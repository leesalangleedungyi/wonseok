from django.urls import path
from . import views

urlpatterns = [


    path('custom_form/',views.custom_form,name='custom_form'),
    path('django_form/',views.django_form,name='django_form'),
    path('musician_create/',views.musician_create,name='musician_create'),
    
]