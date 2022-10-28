from django.urls import path
from . import views

urlpatterns = [
    # User 생성
    path("v1/users/create/", views.UserCreateView.as_view(), name="apis_v1_users_create"),

    # 프로필 사진 삭제
    path("v1/users/profile/delete/", views.ProfileDeleteview.as_view(), name="apis_v1_users_profile_delete"),
    
    # 프로필 사진 변경
    path("v1/users/profile/update/", views.ProfileUpdateView.as_view(), name="apis_v1_users_profile_update"),
]
