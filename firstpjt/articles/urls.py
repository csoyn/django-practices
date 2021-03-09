from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # ~/articles/
    path('', views.index, name='index'),
    # ~/articles/greeting/
    path('greeting/', views.greeting, name='greeting'),
    # ~/articles/dinner/
    path('dinner/', views.dinner, name='dinner'),
    # ~/articles/throw/
    path('throw/', views.throw, name='throw'),
    # ~/articles/catch/
    path('catch/', views.catch, name='catch'),
    # ~/articles/hello/가변이름/가변나이/
    path('hello/<name>/<int:age>/', views.hello, name='hello'),
]