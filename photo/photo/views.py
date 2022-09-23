from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

from .models import Photo
from .forms import PhotoForm

# HttpResponse : 응답 객체
    # 1) 문자열을 담아서 리턴
    # 2) 특정 페이지를 리턴
    #    return HttpResponse(template.render(템플릿, 전달해줄 객체))


# 함수형 뷰
def home(request):  
    return HttpResponse("INDEX")



def photo_list(request):  

    # 사진목록 추출한 후 목록을 보내야 함
    # select * from photo_photo;
    # QuerySet 결과로 나옴
    photos = Photo.objects.all()

    return render(request,"photo_list.html",{"photos":photos})

def photo_post(request):
    """
    PhotoForm 사용하는 방식 
    """
    if request.method =="POST":
        # 사용자 입력값 가져와서 photoform 에 바인딩 시켜주는 역할
        form = PhotoForm(request.POST)
        
        if form.is_valid():
            form.save()
            # 입력 값 데이터 베이스에 저장
        
            # 성공 시 리스트 보여주기
            
            return redirect("photo_list")
    else : 
        form = PhotoForm()
    
    return render(request,"photo_post2.html",{"form":form})



# def photo_post(request):
#     """ forms.py를 사용하지 않고 사용자의 입력값을 하나씩 가져오기"""
#     if request.method =="POST":
#         # 사용자 입력값 가져오기
#         title = request.POST['title']
#         author = request.POST['author']
#         image = request.POST['image']
#         description = request.POST['description']
#         price = request.POST['price']
#         print('사용자 입력값',title,author,image,description,price)
#         # 입력 값 데이터 베이스에 저장
#         photo = Photo(title=title,author=author,image=image,description=description,price=price)
#         photo.save()
#         # 성공 시 리스트 보여주기
        
#         return redirect("photo_list")
    
#     return render(request,"photo_post.html")

def photo_detail(request,pk):
    # pk에 해당하는 게시물 가져오기
    photo = get_object_or_404(Photo,pk=pk)
    # 템플릿을 보여줄 떄 게시물 딸려보내기
    
    return render(request,"photo_detail.html",{"photo":photo})
        
def photo_remove(request,pk):
    print('삭제',pk)
    
    # pk에 해당하는 사진 찾기  
    photo = get_object_or_404(Photo,pk=pk)

    
    # 있으면 삭제하기
    photo.delete()
    # 사진 목록 보기 이동
    return redirect("photo_list")

def photo_edit(request,pk):
    
    ''' PhotoForm사용 
    '''
    #pk에 해당하는 게시물 가져오기 
    object= get_object_or_404(Photo,pk=pk)
    #post 요청시
    if request.method == "POST":
        
        form = PhotoForm(request.POST,instance=object)
        
        if form.is_valid():
            photo = form.save()
            return redirect("photo_detail",pk=photo.pk)


    
        #get으로 요청 시 
    
   
    else:
        
        
        photo = PhotoForm(instance=object)
        
        
    #찾은 게시물을  딸려 보내기
    return render(request,"photo_edit2.html",{"photo":photo})

#def photo_edit(request,pk):
    
    # pk에 해당하는 게시물 가져오기
    photo = get_object_or_404(Photo,pk=pk)

    #post 요청시
    if request.method == "POST":
    # 1. 수정 한 내용 가져오기
        title = request.POST['title']
        author = request.POST['author']
        image = request.POST['image']
        description = request.POST['description']
        price = request.POST['price']
        print('사용자 입력값',title,author,image,description,price)

        # 2. 수정 내용 db에 반영시키기
        photo.title=title
        photo.author=author
        photo.image=image
        photo.description=description
        photo.price=price
        photo.save()
        # 3. 성공하면 상세보기로 이동하기
        return redirect("photo_detail",pk=photo.pk)
    
    #get으로 요청 시 
    
   
    
    #찾은 게시물을  딸려 보내기
    return render(request,"photo_edit.html",{"photo":photo})
