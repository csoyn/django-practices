from django.urls import path
from . import views

app_name = 'fakegoogle'
urlpatterns = [
    # ~/fake/
    path('', views.fake),
]
