from django.shortcuts import redirect, render,get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from tools.utils import get_client_ip

from ..forms import AnswerForm, CommentForm, QuestionForm
from ..models import Answer, Question, Comment, QuestionCount

from django.db.models import Q,Count

def index(request):
    """
    Question 질문목록 추출
    """

    # 사용자가 입력한 검색어 가져오기
    keyword = request.GET.get('keyword','')

    # 사용자가 요청한 페이지 값 가져오기
    page = request.GET.get("page", 1)

    # 사용자가 입력한 정렬기준 가져오기
    so = request.GET.get('so','recent')

    if so == "recommend":
        question_lists = Question.objects.annotate(num_voter = Count('voter')).order_by('-num_voter', '-created_at')
    elif so == "popular":
        question_lists = Question.objects.annotate(num_answer = Count('answer')).order_by('-num_answer', '-created_at')
    else:
        # 전체 목록 추출 - 최신순
        question_lists = Question.objects.order_by("-created_at")

    # 검색결과 리스트 추출
    # subject, content, author 항목들이 검색어와 일치하는 경우를 추출
    # Q : or 조건으로 데이터 조회
    # icontains : 대소문자 구별 없이
    if keyword:
        question_lists = question_lists.filter(
            Q(subject__icontains = keyword) |
            Q(content__icontains = keyword) |
            Q(author__username__icontains = keyword) 
        ).distinct()


    # 전체 목록 안에서 사용자가 요청한 페이지에 대한 목록만 전송
    paginator = Paginator(question_lists, 10)
    question_list = paginator.get_page(page)

    return render(request, "board/question_list.html",{"question_list":question_list,'page':page,'keyword':keyword,'so':so})


def question_detail(request,question_id):
    """
    Question 상세 내용 추출
    """
    question = get_object_or_404(Question, id=question_id)

    ip = get_client_ip(request)
    cnt = QuestionCount.objects.filter(ip=ip, question=question).count()

    if cnt == 0:
        qc = QuestionCount(ip=ip, question=question)
        qc.save()

        if question.read_cnt:
            question.read_cnt += 1
        else:
            question.read_cnt = 1
        question.save()




    # 사용자가 입력한 검색어 가져오기
    keyword = request.GET.get('keyword','')
    # 사용자가 요청한 페이지 값 가져오기
    page = request.GET.get("page", 1)
    # 사용자가 입력한 정렬기준 가져오기
    so = request.GET.get('so','recent')


    return render(request, "board/question_detail.html",{"question":question,'page':page,'keyword':keyword,'so':so})