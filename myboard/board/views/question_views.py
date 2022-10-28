from django.shortcuts import redirect, render,get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from ..forms import AnswerForm, CommentForm, QuestionForm
from ..models import Answer, Question, Comment

@login_required(login_url='users:login')
def question_create(request):
    """
    Question 등록
    """
    if request.method == "POST":
        form = QuestionForm(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()

            return redirect("board:index")
    else:
        form = QuestionForm()

    return render(request, "board/question_create.html",{"form":form})

@login_required(login_url='users:login')
def question_modify(request,question_id):
    """
    Question 수정
    """
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)

        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            # 성공시 detail 
            return redirect("board:question_detail",question_id=question_id)
    else:
        form = QuestionForm(instance=question)

    return render(request, "board/question_modify.html", {"form":form})

@login_required(login_url='users:login')
def question_delete(request, question_id):
    """
    Question 삭제
    """
    question = get_object_or_404(Question, pk=question_id)

    question.delete()
    # 성공시 list 보여주기
    return redirect("board:index")