from django.urls import path
from . import views

urlpatterns = [
    # ~/variable/introduce/가변(글자)/가변(숫자)/
    path('introduce/<name>/<int:age>/', views.introduce),

    # ~/variable/times/가변(숫자)/가변(숫자)/
    path('times/<int:num1>/<int:num2>/', views.times),

    # 원의 반지름을 url에서 가져와서 넓이를 계산
    # ~/variable/area/가변(숫자)/ 
    path('area/<int:r>/', views.area),
]
