from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views


app_name="users"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.signup, name="signup"),

    # 비밀번호 변경
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name="users/password_change.html",
                                            success_url = reverse_lazy("board:index")) ,name="password_change"),
    # path("password_change/done/", auth_views.PasswordChangeDoneView.as_view() ,name="password_change_done"),

    path("password_reset/", views.CustomPasswordResetView.as_view() ,name='password_reset'),
    path("password_reset/done/", views.CustomPasswordResetDoneView.as_view() ,name='password_reset_done'),
    path("reset/<uidb64>/<token>/", views.CustomPasswordResetConfirmView.as_view() ,name='password_reset_confirm'),
    path("reset/done/", views.CustomPasswordResetCompleteView.as_view() ,name='password_reset_complete'),


]
