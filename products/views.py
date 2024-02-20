from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Avg
from django.shortcuts import redirect, reverse
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import Product, Category, Rating
from .forms import ProductForm

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def all_products(request):
    """"A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            if sort_key == 'name':
                sort_key = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sort_key == 'category':
                sort_key = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            products = products.order_by(sort_key)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    for product in products:
        ratings = Rating.objects.filter(product=product)
        average_rating = ratings.aggregate(average=Avg('rating'))['average']
        product.average_rating = round(average_rating) if average_rating else 0

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)
    ratings = Rating.objects.filter(product=product)
    average_rating = ratings.aggregate(average=Avg('rating'))['average']
    average_rating_rounded = round(average_rating) if average_rating else 0

    user_rating = 0
    if request.user.is_authenticated:
        rating = Rating.objects.filter(user=request.user, product_id=product_id).first()
        if rating is not None:
            user_rating = rating.rating

    user_rating = user_rating if user_rating is not None else 0

    star_values = [5, 4, 3, 2, 1]
    stars = [(star_value, user_rating >= star_value) for star_value in star_values]
    print(stars)

    context = {
        'product': product,
        'average_rating': average_rating,
        'user_rating': user_rating,
        'stars': stars,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))

@csrf_exempt
def rate_product(request, product_id):
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        product = get_object_or_404(Product, pk=product_id)
        user = request.user
        ratings = Rating.objects.filter(product=product, user=user)
        if ratings.exists():
            ratings.update(rating=rating_value)
        else:
            Rating.objects.create(product=product, user=user, rating=rating_value)
        return JsonResponse({'message': 'Rating submitted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request'})