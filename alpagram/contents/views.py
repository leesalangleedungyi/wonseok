from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from .models import Content
# def home(request):
#     return render(request, "home.html")

class HomeView(TemplateView):
    template_name = "home.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect("contents")
            
        return super().dispatch(request, *args, **kwargs)


class ContentView(TemplateView):
    template_name = "contents/main.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
            
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        
        context['contents']=Content.objects.filter(user=self.request.user)
        return  context


