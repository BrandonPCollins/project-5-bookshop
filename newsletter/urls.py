from django.urls import path
from .views import subscribe_newsletter, subscription_success

app_name = 'newsletter'

urlpatterns = [
    path('', subscribe_newsletter, name='subscribe_newsletter'),
    path('success/', subscription_success, name='subscription_success'),
]
