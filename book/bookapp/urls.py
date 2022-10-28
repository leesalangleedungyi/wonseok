from django.urls import path
from . import views

urlpatterns = [  
    # 함수형 뷰  
    # path("", views.book_list, name="book_list"),

    # 클래스 뷰
    path("",views.BookListView.as_view(), name="book_list"),

    # 클래스 뷰
    # http://127.0.0.1:8000/book/1000/
    path("<int:pk>/", views.BookDetailView.as_view(),name="book_detail"),

    # 함수형 뷰
    # http://127.0.0.1:8000/book/1000/edit/
    path("<int:pk>/edit/", views.book_update, name="book_edit"),

    # http://127.0.0.1:8000/book/1000/remove/
    path("<int:pk>/remove/", views.book_remove, name="book_remove"),
]
