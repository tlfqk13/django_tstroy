from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.

def register(request):
    if request.method=='POST': # 가입한 정보고 서버로 전달할때,
        user_form=RegisterForm(request.POST)
        if user_form.is_valid():
            user=user_form.save(commit=False) # commit=False는 디비에 저장보다 메모리상에만 객체 생성 
            user.set_password(user_form.cleaned_data['password']) # set_password
            user.save() # 이제 디비에 저장
            return render(request,'registration/login.html',{'user':user}) # 템플릿 렌더링, 
    else:
        user_form=RegisterForm()

    return render(request,'registration/register.html',{'user_form':user_form})
