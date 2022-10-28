from django.urls import path,include
from . import views

app_name = "app1"

urlpatterns = [   
    path('list/', views.list, name="list"),    
    path('detail/', views.detail, name="detail"),    
]
