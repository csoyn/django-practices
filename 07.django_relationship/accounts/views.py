from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm


# DB 유저 정보 생성(CREATE)
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


# DB 유저 세션 생성
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

# DB 유저 세션 삭제
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)

    context = {
        'person': person
    }
    return render(request, 'accounts/profile.html', context)


def followings(request, username):
    person = get_object_or_404(get_user_model(), username=username)

    context = {
        'followings': person.followings.all()
    }
    return render(request, 'accounts/followings.html', context)


def follow(request, person_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    person = get_object_or_404(get_user_model(), pk=person_pk)

    if person != request.user:
        # 대상과 유저가 다를때
        if person.followers.filter(pk=request.user.pk).exists():
            # 이미 팔로워 목록에 있을때
            person.followers.remove(request.user)
        else:
            # 없을때
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)


            


            