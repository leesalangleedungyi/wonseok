from django.urls import path
from . import views

# app_name = "polls"

urlpatterns = [

    # 함수형 뷰 예제
    # http://127.0.0.1:8000/polls/
    # path("", views.index, name="index"),

    # # http://127.0.0.1:8000/polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),

    # # http://127.0.0.1:8000/polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),

    # http://127.0.0.1:8000/polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),


    # 클래스 뷰 
    # http://127.0.0.1:8000/polls/
    path("", views.IndexView.as_view(), name="index"),

    # http://127.0.0.1:8000/polls/5/
    path("<int:pk>/", views.QuestionDetailView.as_view(), name="detail"),

    # http://127.0.0.1:8000/polls/5/results/
    path("<int:pk>/results/", views.QuestionResultView.as_view(), name="results"),

]
