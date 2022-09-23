# 장고의 폼 처리 기능
# 1) 폼 생성에 필요한 데이터를 폼 클래스로 구조화
# 2) 폼 클래스의 데이터를 랜더링하여 html
from dataclasses import fields
from  django import forms
from django.core.exceptions import ValidationError
from .models import Musician
class NameForm(forms.Form):
    name = forms.CharField(max_length=20,label="Your name")
    
    # def clean_name(self) :
    #     # max_length , not null 검증
    #     cleaned_data=super().clean()
        
    #     # 추가 검증
        
    #     name = cleaned_data.get('name') # celand_data['name']
        
    #     if name != '홍길동':
    #         raise ValidationError("이름을 확인해 주세요")
        
    def clean(self) :
        # max_length , not null 검증
        cleaned_data=super().clean()
        
        # 추가 검증
        
        name = cleaned_data.get('name') # celand_data['name']
        
        if name != '홍길동':
            
            self.add_error('name','입력값을 확인해 주세요')
            
            # non_field 에러로 인식
            # raise ValidationError("이름을 확인해 주세요")
        
class MusicianForm(forms.ModelForm):
    
    # 모델 폼을 상속 받을 떄 meta가 꼭 있어야함
    
    class Meta:
        model = Musician
        # exclude = [ 'instrument'] __all__ 사용 후 뺴야할 컬럼은 이렇게 지정하면 됌
        # fields = ['first_name','last_name'...]  쓰고싶은것만 써도 됌
        fields = '__all__'
    
        