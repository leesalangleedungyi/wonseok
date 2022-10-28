from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import BoardForm

from .models import Board


def board_list(request):
    """
    아이디 내림차순 전체 게시물 조회 - boards
    """

    all_boards = Board.objects.order_by("-id")

    page = request.GET.get('page',1)
    # page(전체게시물, 한 페이지에 보여줄 게시물 개수)
    paginator = Paginator(all_boards,10)

    boards = paginator.get_page(page)


    return render(request, "board/list.html", {"boards":boards})


@login_required
def board_write(request):
    """
    get, post BoardForm 이용 / write.html 작성(users에서 했었던 register.html 참고)
    입력 성공 후 게시판 리스트 보여주기
    """
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.writer = request.user
            # 게시물 최종 저장
            board.save()
            # 태그 저장
            form.save_m2m()

            return redirect("list")
    else:
        form = BoardForm()

    return render(request, "board/write.html",{"form":form})


def board_detail(request, pk):
    """
    pk 해당하는 게시물 가져와서 보내기 / detail.html(title,contents,tags)
    """
    board = get_object_or_404(Board, pk=pk)

    return render(request, "board/detail.html", {"board":board})