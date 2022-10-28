from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import Musician

from .forms import MusicianForm, NameForm

def index(request):
    return render(request,"index.html")


def custom_form(request):
    """
    forms 를 이용하지 않는 방식
    """
    if request.method == "POST":
        # name 가져오기
        name = request.POST['name']
        # 프린트
        print(name)
        # 이름이 홍길동이 아닌 경우
        if name != "홍길동":
            return redirect("custom_form")
        else:
            return redirect("index")

    return render(request,"custom_form.html")


def django_form(request):
    """
    is_valid() : 유효성 검증
                 name = forms.CharField(max_length=20)
                 not null, max_length=20 검증

    is_valid() 통과 시 cleaned_data 딕셔너리에 값을 담아 줌
    """

    if request.method == "POST":
        # name 값 가져오기
        form = NameForm(request.POST)
        if form.is_valid():                        
            return redirect("index")
    else:
        form = NameForm()
    return render(request,"django_form.html",{"form":form})


##################### 함수형 뷰

def musician_create(request):
    """
    musician 추가
    """
    if request.method == "POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            # 저장
            form.save()  # 모델폼을 상속받은 상태이기 때문에 가능
            return redirect("index")
    else:
        form = MusicianForm()
    return render(request,"musician_register.html",{"form":form})


def musician_list(request):
    """
    musician 전체 리스트 보기 - get 방식
    """
    musician_list = Musician.objects.all()

    # musician_list.html
    return render(request,"musician_list.html",{"musician_list":musician_list})

def musician_detail(request, pk):
    """
    pk에 해당하는 musician 정보 추출 - 상세조회
    """
    musician = get_object_or_404(Musician, pk=pk)

    # musician_detail.html
    return render(request, "musician_detail.html",{"musician":musician})


def musician_edit(request, pk):
    """
    pk에 해당하는 musician 정보 추출 - 수정
    """
    musician = get_object_or_404(Musician, pk=pk)

    # get, post 따로 작성
    if request.method == "POST":
        form = MusicianForm(request.POST,instance=musician)
        if form.is_valid():
            musician = form.save()
            return redirect("musician_detail",pk=musician.pk)
    else:
        form = MusicianForm(instance=musician)

    # musician_edit.html
    return render(request, "musician_edit.html",{"form":form})


def musician_remove(request,pk):
    """
    pk에 해당하는 musician 삭제
    """
    musician = get_object_or_404(Musician, pk=pk)
    musician.delete()

    # 삭제 후 리스트로 이동
    return redirect("musician_list")



####################### 
# 클래스 기반의 뷰 
# 1. 제네릭 display view(DetailView, ListView)    
#######################

class MusicianListView(ListView):
    """
    함수형 뷰 - musician_list() 와 같은 역할
    """
    model = Musician
    template_name = "musician_list.html" # 생략 가능(templates/exam/musician_list.html 이라면)


class MusicianDetailView(DetailView):
    """
    함수형 뷰 - musician_detail() 와 같은 역할
    """
    model = Musician
    template_name = "musician_detail.html" # 생략 가능(templates/exam/musician_detail.html 이라면)


####################### 
# 클래스 기반의 뷰 
# 2. 제네릭 Edit view(CreateView, UpdateView, DeleteView)    
#######################

class MusicianCreateView(CreateView):
    """
    함수형 뷰 - musician_create()와 같은 역할
    """
    form_class = MusicianForm
    template_name = "musician_register.html" # 생략 가능(templates/exam/musician_register.html 이라면)
    success_url =  reverse_lazy("musician_list_cls")

class MusicianUpdateView(UpdateView):
    """
    함수형 뷰 - musician_edit()와 같은 역할
    """
    model = Musician
    fields = "__all__"
    template_name = "musician_edit.html"
    success_url =  reverse_lazy("musician_list_cls")

class MusicianDeleteView(DeleteView):
    """
    함수형 뷰 - musician_remove()와 같은 역할
    """
    model=Musician
    success_url =  reverse_lazy("musician_list_cls")
    # template_name = "musician_remove.html"  exam/musician_confirm_delete.html

    # post로 들어왔을 때만 삭제로 정의되어 있기 때문에 추가
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)