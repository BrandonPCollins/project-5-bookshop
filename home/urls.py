from django.urls import path
from . import views
from products.views import product_detail

urlpatterns = [
    path('', views.index, name='home'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
]
