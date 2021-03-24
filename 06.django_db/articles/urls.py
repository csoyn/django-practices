from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # ~/articles/몇번게시물/
    path('<int:article_pk>/', views.detail, name='detail'),
]
