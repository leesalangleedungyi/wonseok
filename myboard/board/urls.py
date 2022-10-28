from django.urls import path

from .views import base_views, question_views, answer_views, comment_views, voter_views

app_name = "board"

urlpatterns = [
    
    #### 질문

    # http://127.0.0.1:8000/board/
    path('',base_views.index, name="index"),

    # http://127.0.0.1:8000/board/1/
    path('<int:question_id>/',base_views.question_detail, name="question_detail"),
    
    # http://127.0.0.1:8000/board/question/create/
    path('question/create/',question_views.question_create, name="question_create"),

    # http://127.0.0.1:8000/board/question/modify/1/
    path('question/modify/<int:question_id>/',question_views.question_modify, name="question_modify"),
    
    # http://127.0.0.1:8000/board/question/delete/1/
    path('question/delete/<int:question_id>/',question_views.question_delete, name="question_delete"),


    ###### 답변 

    # http://127.0.0.1:8000/board/answer/create/1/
    path('answer/create/<int:question_id>/',answer_views.answer_create, name="answer_create"),

    # http://127.0.0.1:8000/board/answer/modify/1/
    path('answer/modify/<int:answer_id>/',answer_views.answer_modify, name="answer_modify"),

    # http://127.0.0.1:8000/board/answer/delete/1/
    path('answer/delete/<int:answer_id>/',answer_views.answer_delete, name="answer_delete"),


    #### Comment
    # http://127.0.0.1:8000/board/comment/create/question/1/
    path('comment/create/question/<int:question_id>/',comment_views.comment_create_question, name="comment_create_question"),


    # http://127.0.0.1:8000/board/comment/modify/question/1/
    path('comment/modify/question/<int:comment_id>/',comment_views.comment_modify_question, name="comment_modify_question"),

    # http://127.0.0.1:8000/board/comment/delete/question/1/
    path('comment/delete/question/<int:comment_id>/',comment_views.comment_delete_question, name="comment_delete_question"),
   
    path('comment/create/answer/<int:answer_id>/',comment_views.comment_create_answer, name="comment_create_answer"),
    path('comment/modify/answer/<int:comment_id>/',comment_views.comment_modify_answer, name="comment_modify_answer"),
    path('comment/delete/answer/<int:comment_id>/',comment_views.comment_delete_answer, name="comment_delete_answer"),



    #### 추천
    # http://127.0.0.1:8000/board/vote/question/1/
    path('vote/question/<int:question_id>/',voter_views.vote_question, name="vote_question"),
    path('vote/answer/<int:answer_id>/',voter_views.vote_answer, name="vote_answer"),
]
