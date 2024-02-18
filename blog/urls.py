from django.urls import path
from .views import post_list, post_detail
from . import views

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    ]