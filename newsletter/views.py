from django.shortcuts import render, redirect
from .forms import NewsletterSubscriptionForm

def subscribe_newsletter(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newsletter:subscription_success')
    else:
        form = NewsletterSubscriptionForm()
    return render(request, 'subscribe_newsletter.html', {'form': form})

def subscription_success(request):
    return render(request, 'subscription_success.html')
