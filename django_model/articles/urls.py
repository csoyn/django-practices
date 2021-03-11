from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # ~/articles/ : 전체 게시글 조회
    path('', views.index, name='index'),

    # ~/articles/게시물pk/ : 상세 페이지
    path('<int:pk>/', views.detail, name='detail'),

    # ~/articles/new/ : 글 작성하는 페이지를 랜더
    path('new/', views.new, name='new'),

    # ~/articles/create/ : DB에 반영! (CREATE)
    path('create/', views.create, name='create'),

    # ~/articles/게시물pk/edit/ : 글 수정하는 페이지를 랜더
    path('<int:pk>/edit/', views.edit, name='edit'),

    # ~/articles/게시물pk/update/ : DB에 반영! (UPDATE)
    path('<int:pk>/update/', views.update, name='update'),

    # ~/articles/게시물pk/delete/ : DB에서 삭제!
    path('<int:pk>/delete/', views.delete, name='delete'),
]
