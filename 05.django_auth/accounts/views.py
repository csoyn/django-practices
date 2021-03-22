from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST

# DB 유저 세션 생성(CREATE)
def login(request):
    # 로그인되어 있다면
    # 로그인 페이지를 볼 필요도 없고 실제 로그인 동작도 필요없다.
    # print(dir(request.user))
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # next 파라미터는 여기서 사용!
            # ?next=/articles/create/
            # A or B : 단축평가를 활용
            # A : request.GET.get('next') 가 있는 경우 B를 확인하지 않고 A로 이동
            # A가 없는 경우에는 B로 간다
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        # 개발자가 생성한 form class 사용 X 
        # => 장고가 제공하는 form class 사용 O
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


# DB 유저 세션 삭제(DELETE)
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


# DB 유저 정보 생성(CREATE)
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # 회원 가입 완료
            user = form.save()
            # 로그인
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


# DB 유저 정보 삭제(DELETE)
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('accounts:login')