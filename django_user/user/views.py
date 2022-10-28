from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from .forms import UserForm

def index(request):
    return render(request,"index.html")


def signup(request):
    """
    회원가입
    """

    if request.method == "POST":
        # post로 넘어오는 값에 대해 UserForm 바인딩 처리        
        form = UserForm(request.POST)

        # 폼 검증
        if form.is_valid():
            # 저장
            form.save()
            return redirect("user:login")
    else:
        form = UserForm()

    return render(request, "user/signup.html",{"form":form})

# def custom_login(request):
#     """
#     커스텀 로그인 - 직접 구현
#     """
#     if request.method == "POST":
#         # 아이디(사용자이름)와 비밀번호 가져오기
#         username = request.POST['username']
#         password = request.POST['password']

#         # 인증(로그인 값이 정확한가?)
#         user = authenticate(request,username=username,password=password)

#         # 정확하면 세션에 값을 담게 됨
#         if user is not None:
#             login(request, user)
#             return redirect("user:index")

#     return render(request,"user/login.html")

# def custom_logout(request):
#     """
#     커스텀 로그아웃 - 직접 구현
#     """
#     # 세션 해제
#     logout(request)
#     return redirect("index")


#################################
#  장고 회원 URL 이용하기
#################################

class CustomPassWordChangeView(PasswordChangeView):
    success_url = reverse_lazy("user:index")

