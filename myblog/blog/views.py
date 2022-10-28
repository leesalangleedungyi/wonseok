from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import JsonResponse

from .forms import PostForm

from .models import Comment, Post

def posts_list(request):
    """
    블로그 전체목록
    """
    # 전체목록
    # Post.objects.all()

    # order by
    posts = Post.objects.order_by("-created_at")

    return render(request,"blog/blog_list.html",{"posts":posts})

@login_required(login_url="login")
def posts_write(request):
    """
    블로그 작성 - get(글 쓸수 있는 페이지 보여주기), post(글 등록)    
    """
    if request.method == "POST":
        # form 에 내용담기
        form = PostForm(request.POST,request.FILES)
        # 유효성 검사
        if form.is_valid():
            # save()
            # form 안에는 user 정보가 없음
            post = form.save(commit=False)
            # user 정보 가져오기(세션)
            post.user = request.user
            post.save()
            # 태그 저장
            form.save_m2m()

            # 이동
            return redirect("posts_list")
    else:
        form = PostForm()

    return render(request, "blog/post_write.html",{"form":form})


def posts_detail(request,pk):
    """
    pk에 해당하는 블로그 글 가져오기
    """
    post = get_object_or_404(Post, pk=pk)

    # 현재 게시물에 로그인한 사용자가 좋아요를 눌렀는지에 대한 정보 필요
    is_liked = False

    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    # post_detail.html
    return render(request,"blog/post_detail.html",{"post":post, "is_liked":is_liked})


@require_POST
@login_required(redirect_field_name="next")
def comment_create(request):
    """
    댓글 등록
    """
    errors = []
    if request.method == "POST":
        # 폼에서 넘어오는 값 2개 가져오기
        post_id = request.POST.get("post_id").strip()
        content = request.POST.get("content").strip()

        if content:
            # 댓글 생성
            # comment = Comment(user=request.user,post=post_id,content=content)
            # comment.save()

            Comment.objects.create(user=request.user,post_id=post_id,content=content)
            return redirect("post_detail", pk=post_id)
        else:
            # 화면 쪽에 에러 메세지 전송
            messages.error(request,"댓글을 입력해 주세요")
            return redirect("post_detail", pk=post_id)


@login_required
@require_POST
def post_like(request):
    """
    사용자가 좋아요를 클릭 시 처리하는 부분
    좋아요를 추가 or 차감
    """

    # 현재 게시물 번호 가져온 후 게시물 정보 추출
    post = get_object_or_404(Post,id=request.POST.get("id"))

    # 게시물에 현재 로그인 사용자가 누른 좋아요가 있는지 확인하기
    is_liked = post.likes.filter(id=request.user.id).exists()

    # 좋아요가 눌린 상태라면 좋아요 해제 / 좋아요가 아닌 상태라면 좋아요 추가
    is_liked_change = False
    if is_liked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        is_liked_change = True

    # 리턴
    return JsonResponse({"likes": post.likes.count(), "is_liked":is_liked_change})
