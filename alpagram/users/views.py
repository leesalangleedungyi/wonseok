from django.shortcuts import render,redirect
from .models import Context
from .forms import RegisterForm
from django.contrib.auth import authenticate,login
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
class ProfileView(TemplateView):
    """
    프로필 정보 보여주기 - 로그인 필요
    """
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs) :
        
        contents = Content.object.filter(user=self.request.user)
        context['contents'] = contents
        return context





# 기존방식 - 지금은 사용하지 않음
def register(request):
    """
    회원가입 - post
    """
    if request.method == "POST":
        # RegisterForm 이용
        # 회원가입 완료 후 로그인 처리까지
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # 비밀번호 따로 저장
            user.set_password(form.cleaned_data['password'])
            user.save()

            # 로그인 처리
            login_user = authenticate(username = form.cleaned_data['email'], password=form.cleaned_data['password'])

            login(request, login_user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "home.html", {"form":form})