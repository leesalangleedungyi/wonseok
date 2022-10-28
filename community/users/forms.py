from django import forms
from .models import CustomUser


class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
    password2 = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'phone') # 튜플 or 리스트 
        
    # 비밀번호와 비밀번호 확인이 동일한지 검증
    # clean() or clean_필드명()
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1  != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
        return password2

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user