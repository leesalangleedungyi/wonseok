from django.shortcuts import render

def detail(request):
    return render(request, "app2/detail.html")
