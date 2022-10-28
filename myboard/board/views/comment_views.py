from django.shortcuts import redirect, render,get_object_or_404,resolve_url
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from ..forms import AnswerForm, CommentForm, QuestionForm
from ..models import Answer, Question, Comment

@login_required(login_url='users:login')
def comment_create_question(request,question_id):
    """
    질문 댓글 등록
    """

    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.question = question
            comment.save()
            # return redirect("board:question_detail",question_id=question_id)
            return redirect("{}#comment_{}".format(resolve_url("board:question_detail",question_id=question_id),comment.id))
    else:
        form = CommentForm()
    return render(request, "board/comment_create.html",{"form":form})

@login_required(login_url='users:login')
def comment_modify_question(request,comment_id):
    """
    질문 댓글 수정 => 템플릿은 comment_create 사용
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            # return redirect("board:question_detail",question_id=comment.question.id)
            return redirect("{}#comment_{}".format(resolve_url("board:question_detail",question_id=comment.question.id),comment.id))

    else:
        form = CommentForm(instance=comment)
        
    return render(request, "board/comment_create.html",{"form":form})

@login_required(login_url='users:login')
def comment_delete_question(request,comment_id):
    """
    질문 댓글 삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()

    return redirect("board:question_detail",question_id=comment.question.id)


@login_required(login_url='users:login')
def comment_create_answer(request, answer_id):
    """
    답변 댓글 등록
    """

    answer = get_object_or_404(Answer, pk=answer_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.answer = answer
            comment.save()
            # return redirect("board:question_detail",question_id=comment.answer.question.id)
            return redirect("{}#comment_{}".format(resolve_url("board:question_detail",question_id=comment.answer.question.id),comment.id))
    else:
        form = CommentForm()
    return render(request, "board/comment_create.html",{"form":form})

@login_required(login_url='users:login')
def comment_modify_answer(request,comment_id):
    """
    답변 댓글 수정 => 템플릿은 comment_create 사용
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            # return redirect("board:question_detail",question_id=comment.answer.question.id)
            return redirect("{}#comment_{}".format(resolve_url("board:question_detail",question_id=comment.answer.question.id),comment.id))
    else:
        form = CommentForm(instance=comment)
        
    return render(request, "board/comment_create.html",{"form":form})

@login_required(login_url='users:login')
def comment_delete_answer(request,comment_id):
    """
    질문 댓글 삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()

    return redirect("board:question_detail",question_id=comment.answer.question.id)