from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Answer, Question

from django.contrib import messages

@login_required(login_url='users:login')
def vote_question(request, question_id):
    """
    질문 추천 등록 : 본인이 작성한 글은 추천하지 못하도록 함/성공-detail
    """

    question = get_object_or_404(Question, pk=question_id)

    if question.author == request.user:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        question.voter.add(request.user)

    return redirect("board:question_detail", question_id=question_id)


@login_required(login_url='users:login')
def vote_answer(request, answer_id):
    """
    답변 추천 등록 : 본인이 작성한 글은 추천하지 못하도록 함/성공-detail
    """

    answer = get_object_or_404(Answer, pk=answer_id)

    if answer.author == request.user:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        answer.voter.add(request.user)

    return redirect("board:question_detail", question_id=answer.question.id)