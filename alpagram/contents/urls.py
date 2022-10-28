from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.ContentView.as_view(), name="contents")
]
