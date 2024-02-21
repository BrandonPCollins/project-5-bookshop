from django.shortcuts import render, redirect
from .forms import NewsletterSubscriptionForm
from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(email):
    subject = 'Newsletter Subscription Confirmation'
    message = 'Thank you for subscribing to our newsletter!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def subscribe_newsletter(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            send_confirmation_email(form.cleaned_data.get('email'))
            return redirect('newsletter:subscription_success')
    else:
        form = NewsletterSubscriptionForm()
    return render(request, 'subscribe_newsletter.html', {'form': form})

def subscription_success(request):
    return render(request, 'subscription_success.html')