"""firstpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# articles라는 앱의 views 파이썬 파일을 불러오고
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # ~/articles/
    # >>> articles.urls <<<
    # # 불러온 views 파일의 특정 함수를 개발자가 의도한 url이랑 연결
    # path('', views.index, name='index'),
    # # greeting/ 으로 접근하면, views의 greeting이라는 함수랑 연결할래!
    # path('greeting/', views.greeting, name='greeting'),
    # path('dinner/', views.dinner, name='dinner'),
    # # HTML form tag
    # path('throw/', views.throw, name='throw'),
    # path('catch/', views.catch, name='catch'),
    # # Variable Routing : < >
    # path('hello/<name>/<int:age>/', views.hello, name='hello'),

    # name : Naming URL Patterns => url에 별명붙이기!
    # template에서는 {% url %} 태그를 사용한다!

    # url Namespace!!
    # app이 분리되었을때 url 별명이 같다면?

    # url 분리하기 : include('앱이름.urls')
    # ~/pages/
    path('pages/', include('pages.urls')),
    # ~/articles/
    path('articles/', include('articles.urls')),
]
