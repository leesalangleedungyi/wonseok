from django.shortcuts import render,get_object_or_404,redirect

from .forms import TodoForm
from .models import Todo

# Create your views here.
def index(request):
    return render(request,"index.html")

def todo_list(request):
    """
    todo 목록 추출
    """
    
    #전체 리스트 가져오기
   # todos = Todo.objects.all()
    
    #조건이 들어간 리스트 가져오기
    
    todos = Todo.objects.filter(complete=False)
    
    return render(request,"todo_list.html",{"todos":todos})


#상세보기
def todo_detail(request,pk):
    
    todo = get_object_or_404(Todo,pk=pk)
    return render(request,"todo_detail.html",{"todo":todo})

#등록하기
def todo_create(request):
    
    if request.method == "POST":
        form=TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect("todo_detail",pk=todo.pk)
            
    else :
        form=TodoForm()
    
    
    return render(request,'todo_register.html',{"form":form})
#

def todo_edit(request,pk):
    
    '''pk에 해당하는 todo 가져오기 / 보내기'''
    
    todo = get_object_or_404(Todo,pk=pk)
    
    if request.method=="POST":
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm(instance=todo)
    return render(request,"todo_edit.html",{"form":form})

def todo_done(request,pk):
    
    '''
    pk에 해당하는 todo의 complete를 true 로변 경 후 리스트로 돌아가기'''
    # todo 가져오기
    todo = get_object_or_404(Todo,pk=pk)
    
    todo.complete = True
    todo.save()

    #리스트로 돌아가기
    return redirect("todo_list")

def done_list(request):
    #완료 목록 추출 / 보내기
    
    dones = Todo.objects.filter(complete=True)

    return render(request,"done_list.html",{"dones":dones})
    