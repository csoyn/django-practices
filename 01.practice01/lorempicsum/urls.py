from django.urls import path
from . import views

app_name = 'lorempicsum'
urlpatterns = [
    # ~/images/
    path('', views.image, name='image')
]