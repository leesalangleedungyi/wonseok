from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/user/register/
    path('register/', views.user_register, name="user_register"),

]
