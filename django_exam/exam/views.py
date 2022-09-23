from errno import ESTALE
from django.shortcuts import render,get_object_or_404,redirect
from .forms import MusicianForm,NameForm


def index(request):
    return render(request,"index.html")

def custom_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        if name != '홍길동':
            return redirect('custom_form')
        else:
            return redirect("index")
    
    return render(request,"custom_form.html")


def django_form(request):

        # is.vaild() -> 유효성 검증
        # 변수에 넣은게 맞는지 확인해줌
        # is.valid() 통과 시 cleaned_data 딕셔너리에 값을 담아 줌
        if request.method == 'POST':
            form = NameForm(request.POST)
            if form.is_valid():
                return redirect('index')
        else:
            form = NameForm()
        return render(request,"django_form.html",{'form':form})
    
def musician_create(request):
    
    '''
    추가
    '''
    form = MusicianForm(request.POST)
    if request.method == "POST":
        form.save()
        return redirect('index')
    else :
        form = MusicianForm()
    
    return render(request,"musician_register.html",{"form":form})