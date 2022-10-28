from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

app_name = "user"

urlpatterns = [
    # http://127.0.0.1:8000/user/
    path("", views.index,name="index"),

    #  http://127.0.0.1:8000/user/signup/
    path("signup/", views.signup,name="signup"),

    #  http://127.0.0.1:8000/user/login/
    # path("login/", views.custom_login,name="login"),

    #  http://127.0.0.1:8000/user/logout/
    # path("logout/", views.custom_logout,name="logout"),


    # 장고의 auth.urls 이용을 하되 필요한 부분만 연결하기
    # http://127.0.0.1:8000/user/login/
    # template_name 을 지정하지 않으면 registration/login.html 로 감
    path("login/", auth_views.LoginView.as_view(template_name="user/login.html"), name="login"),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # http://127.0.0.1:8000/user/password_change/
    # 비밀번호 변경 성공하는 경우  path( "password_change/done/",user/password_change/done/ name="password_change_done") url 필요함
    # path("password_change/", auth_views.PasswordChangeView.as_view(template_name="user/password_change.html"), name="password_change")
    
    # 부모 클래스를 상속받아 필요한 부분만 변경
    path("password_change/", views.CustomPassWordChangeView.as_view(template_name="user/password_change.html"), name="password_change")
]
