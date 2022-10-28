from django.shortcuts import redirect, render

from django.views.generic.base import TemplateView

from .forms import RegisterForm


class HomeView(TemplateView):
    template_name = "home.html"


def register(request):
    """
    get, post
    """
    if request.method == "POST":
        # post 넘어온 데이터에 폼에 담기
        form = RegisterForm(request.POST)
        # form 검증
        if form.is_valid():
            # save
            form.save()
            # home 이동
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form":form})

