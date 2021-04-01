from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # ~/articles/
    path('', views.index, name='index'),

    # ~/articles/create/
    path('create/', views.create, name='create'),

    # ~/articles/몇번게시물/
    path('<int:article_pk>/', views.detail, name='detail'),

    # ~/articles/몇번게시물/comments/
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),

    # ~/articles/몇번게시물/comments/몇번댓글/delete/
    path(
        '<int:article_pk>/comments/<int:comment_pk>/delete/',
        views.comments_delete,
        name='comments_delete'
    ),

    # ~/게시물/몇번/좋아요/
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
