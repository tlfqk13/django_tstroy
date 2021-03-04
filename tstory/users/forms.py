from django import forms
from django.core.exceptions import ValidationError
from .models import User


class RegisterForm(forms.ModelForm):
    # 회원가입 폼
    # 장고에서는 HTML 입력요소를 widget 이라고 말한다

    password = forms.CharField(label='password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fileds = {'username', 'first_name', 'last_name', 'gender', 'email'}

    # 유효성 검사
    def clean_confirm_password(self):
        cd = self.cleande_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다')

        return cd['cofirm_password']
