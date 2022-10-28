from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/blog/post/
    path('post/', views.posts_list, name="posts_list"),
    path('post/write/', views.posts_write, name="post_write"),
    path('post/<int:pk>/', views.posts_detail, name="post_detail"),
    path('comment/create/', views.comment_create, name="comment_create"),
    path('post_like/', views.post_like, name="post_like"),
]
