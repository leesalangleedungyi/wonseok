from django.urls import path
from . import views

urlpatterns = [
    path("custom_form/",views.custom_form,name="custom_form"),
    path("django_form/",views.django_form,name="django_form"),

    # musician 함수형 뷰
    path("musician_create/",views.musician_create,name="musician_create"),
    path("musician_list/",views.musician_list,name="musician_list"),
    path("musician_detail/<int:pk>/",views.musician_detail,name="musician_detail"),
    path("musician_edit/<int:pk>/",views.musician_edit,name="musician_edit"),
    path("musician_remove/<int:pk>/",views.musician_remove,name="musician_remove"),

    # musician 클래스 뷰
    path("musician_list_cls/",views.MusicianListView.as_view(),name="musician_list_cls"),
    path("musician_detail_cls/<int:pk>/",views.MusicianDetailView.as_view(),name="musician_detail_cls"),
    path("musician_create_cls/",views.MusicianCreateView.as_view(),name="musician_create_cls"),
    path("musician_edit_cls/<int:pk>/",views.MusicianUpdateView.as_view(),name="musician_edit_cls"),
    path("musician_remove_cls/<int:pk>/",views.MusicianDeleteView.as_view(),name="musician_remove_cls"),
]
