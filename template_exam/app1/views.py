from django.shortcuts import render

def list(request):
    return render(request, "app1/list.html")

def detail(request):
    return render(request, "app1/detail.html")
