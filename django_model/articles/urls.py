from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # ~/articles/ : 전체 게시글 조회
    path('', views.index, name='index'),

    # ~/articles/new/ : 글 작성하는 페이지를 랜더
    path('new/', views.new, name='new'),

    # ~/articles/create/ : DB에 반영하는 동작
    path('create/', views.create, name='create'),
]
