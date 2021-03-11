from django.urls import path
from . import views

urlpatterns = [
    # ~/fakenaver/
    path('', views.fake),    
]
