from django import forms
from .models import CustomUser

# RegisterForm(CustomUser 모델 폼)
class RegisterForm(forms.ModelForm):

    password = forms.CharField(label="비밀번호",widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email','name','nickname')