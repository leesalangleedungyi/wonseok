from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    # 기존방식
    # path("register/", views.register, name="register"),


    # 장고의 로그인, 로그아웃 이용
    path("login/", auth_views.LoginView.as_view(template_name="home.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("profile/", views.ProfileView.as_view(), name="profile"),

]
