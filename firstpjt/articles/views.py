from django.shortcuts import render
import random

# parameter : request
def index(request):
    # url : ~/index/ 로 접근했을 때
    # 동작하는 함수

    # 어떤 동작? : 렌더하기!
    return render(request, 'articles/index.html')


def greeting(request):
    name = 'tony'
    foods = ['apple', 'banana']
    context = {
        'name': name,
        'foods': foods,
    }
    return render(request, 'articles/greeting.html', context)


def dinner(request):
    menu = ['김치찌개', '청국장', '짬뽕', '스테이크']
    context = {
        'my_dinner': random.choice(menu),
        'menu': menu,
    }
    return render(request, 'articles/dinner.html', context)


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    context = {
        'message': request.GET.get('message') 
    }
    return render(request, 'articles/catch.html', context)


# variable routing : 2번째 파라미터!
def hello(request, name, age):
    print(name)
    print(type(age))
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'articles/hello.html', context)