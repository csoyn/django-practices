from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    # ~/pages/
    path('', views.index, name='index'),
    # ~/pages/new/
    # path('new/', views.new),
    # path('something/anything/', )
]
