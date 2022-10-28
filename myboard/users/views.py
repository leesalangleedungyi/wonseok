from django.shortcuts import redirect, render
from .forms import UserForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("users:login")

            # 로그인 처리까지 구현한다면?
            # 아이디와 비밀번호 가져오기
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            # 인증
            user = authenticate(request,username=username,password=password)

            if user is not None:
                # 로그인
                login(request, user)
            return redirect("board:index")

    else:
        form = UserForm()        
    return render(request, "users/register.html",{"form":form})


class CustomPasswordResetView(PasswordResetView):
    template_name="users/password_reset_form.html"
    success_url = reverse_lazy("users:password_reset_done")

    email_template_name = "users/password_reset_email.txt"

    #
    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            messages.info(self.request, "이메일을 확인해 주세요")
            return redirect("users:password_reset")



class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "users/password_reset_done.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "users/password_reset_confirm.html"
    success_url=reverse_lazy("users:password_reset_complete")

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "users/password_reset_complete.html"