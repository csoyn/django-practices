from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def index(request):
    """
    유저 목록을 출력하는 페이지를 랜더하는 함수
    """
    # User Model Class
    User = get_user_model()
    # Instance
    users = User.objects.all()
    context = {
        'form': AuthenticationForm(),
        'users': users
    }
    return render(request, 'accounts/index.html', context)


def signup(request):
    """
    1. GET : 회원가입 작성을 위한 페이지를 랜더.
    2. POST : 유저를 생성하는 기능을 수행한다.
    """
    if request.method == 'POST':
        # form instance
        form = UserCreationForm(request.POST)
        # validation
        if form.is_valid():
            # 저장
            user = form.save()
            return redirect('accounts:index')
    else:
        # form instance <= Form Class
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('accounts:index')


