from django.urls import path
from .views import post_list, post_detail, delete_comment
from . import views

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    ]