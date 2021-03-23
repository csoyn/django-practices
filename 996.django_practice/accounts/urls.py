from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # ~/accounts/ : 유저 목록을 보여준다!
    path('', views.index, name='index'),

    # ~/accounts/signup/
    path('signup/', views.signup, name='signup'),

    # ~/accounts/login/
    path('login/', views.login, name='login'),
]
