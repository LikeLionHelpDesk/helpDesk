<<<<<<< HEAD
from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import UserForm
from account.models import Profile
from django.contrib.auth.models import User
=======
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
>>>>>>> 14ae95d... first commit

# Create your views here.
def signup(request):
    if request.method == 'POST':    
        form = UserForm(request.POST)
<<<<<<< HEAD
=======
        print(form.data)
        print(form.is_valid)
        print(form.is_valid())
        print(form.errors)
>>>>>>> 14ae95d... first commit
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # 폼의 입력값을 개별적으로 얻고 싶은 경우에 사용하는 함수
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
<<<<<<< HEAD
=======
            print(request)
>>>>>>> 14ae95d... first commit
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form' : form})