from django.shortcuts import render
from products.models import Product

def index(request):
    """" A view that displays the index page """
    featured_products = Product.objects.filter(featured=True)
    return render(request, 'home/index.html', {'featured_products': featured_products})

def about(request):
    """" A view that displays the about page """
    return render(request, 'home/about.html')