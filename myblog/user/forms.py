from tkinter import Widget
from django import forms
from django import forms

from .models import User

class RegisterForm(forms.ModelForm):

    password = forms.CharField(label="password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="confirm_password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','gender','email']

    # clean() : 유효성 검증
    # clean_필드명() : 지정된 필드에 대한 유효성 검증
    def clean_confirm_password(self):
        # cleaned_data : 장고가 유효성 검증을 통과한 데이터를 담아두는 딕셔너리
        cleaned_data = self.cleaned_data
        
        if cleaned_data['password'] != cleaned_data['confirm_password']:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다")

        return cleaned_data['confirm_password']
    