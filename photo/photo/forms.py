from socket import fromshare
from django import forms
from .models import Photo

# form 생성시 form.Form (일반폼) or 
# form.ModelForm(모델폼) 상속 받으면서 만들 수 있음


class PhotoForm(forms.ModelForm):
    
    #장고 폼은 내부 클래스로 반드시 Meta 가져아함
    class Meta:
        # 폼과 연결 할 모델
        
        model = Photo
        
        # 모델에서 사용할 필드 지정
        fields = ['title','author','image','description','price'] #fields = _all_ 쓰면 전체 지정
        
    