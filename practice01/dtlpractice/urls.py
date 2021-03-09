from django.urls import path
from . import views


urlpatterns = [
    # ~/dtlpractice/
    path('', views.dtlpractice),
]
