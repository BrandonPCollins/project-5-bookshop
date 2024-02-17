from django.db import models
from django.contrib import admin
from .models import NewsletterSubscription
from django.core.mail import send_mail

class Newsletter(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()

class NewsletterAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        subscribers = NewsletterSubscription.objects.values_list('email', flat=True)
        sender_email = 'bpcollins1995@gmail.com' 
        for subscriber in subscribers:
            send_mail(obj.subject, obj.message, sender_email, [subscriber], fail_silently=False)

class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email',)  # Display the email field in the admin list view

admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)  