from django.urls import path

from . import views


urlpatterns = [  
    path('list/', views.board_list, name="list"),
    path('write/', views.board_write, name="write"),
    path('detail/<int:pk>/', views.board_detail, name="detail"),
]