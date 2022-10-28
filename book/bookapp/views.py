from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView

from .forms import BookForm
from .models import Book

def index(request):
    return render(request, "index.html")

def book_list(request):
    book_list = Book.objects.all()
    return render(request, "bookapp/book_list.html",{"book_list":book_list})


# 도서전체목록 클래스 뷰 작성
class BookListView(ListView):
    model = Book

# 도서상세정보 클래스 뷰 작성
class BookDetailView(DetailView):
    model =  Book
    

# 함수형 뷰
def book_update(request,pk):

    book = get_object_or_404(Book,pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect("book_detail",pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, "bookapp/book_edit.html",{"form":form})


def book_remove(request,pk):
    """
    도서목록 삭제 
    """
    book = get_object_or_404(Book, pk=pk)

    book.delete()

    return redirect("book_list")
