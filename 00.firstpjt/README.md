# Django Intro

## 설치

```shell
# 최신 버전
$ pip install django


# 버전 명시
$ pip install django==3.0.8
```

## 버전 확인

```shell
$ python -m django --version
```

## 프로젝트 생성

```shell
# django-admin startproject 프로젝트이름 경로
# . 을 적게되면 현재 경로에 바로 생성
# 안쓰면 폴더 하나 더 만들고 그 안에 생성
$ django-admin startproject firstpjt .
# $ python -m django startproject firstpjt .
```

## gitignore 작성하기

`.gitignore`

+ `README.md`

## 프로젝트 폴더 구성

`settings.py`

- django의 설정 사항

`urls.py`

- url과 함수를 연결

`asgi.py`

- django가 비동기식 웹 서버와 연결하는 것을 설정

`wsgi.py`

- 웹 서버와 연결하는 것을 설정

## 프로젝트 실행 🚀

```shell
# 현재 경로에 manage.py가 있는지 확인!
# 프로젝트 생성 이후에는 manage.py한테 전부 시킨다!
$ python manage.py runserver
```

## 애플리케이션 생성

```shell
# python manage.py startapp 앱이름
$ python manage.py startapp articles
```

## 애플리케이션 등록

> 앱 생성이후에는 반드시 등록! (잊어버리기 전에!!!)
>
> 반드시 생성 후에 등록! (순서를 잘 지키자!)

```python
# 프로젝트메인폴더/settings.py >>> INSTALLED_APPS 에 등록!
# firstpjt/settings.py

INSTALLED_APPS = [
    # 사용자 생성 앱
    'articles',

    # 3rd
    
    # built-in
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## 애플리케이션 폴더

`migrations/`

- 마이그레이션 파일들이 들어감

`templates/`

- 탬플릿 폴더 (생성해야함!)
- `s` 오타주의!

`urls.py`

- 생성해야함! (url을 분리할때!)

`admin.py`

- 관리자 페이지를 위한 설정

`models.py`

- 앱에서 사용하는 모델을 정의

`views.py`

- url이랑 연결 할 함수들을 정의

`tests.py`

- 테스트 코드를 작성

`apps.py`

- 앱에 관한 설정


---

## 요청 처리하기

> HTTP request에 따라 각기 다른 동작을 결정
>
> - 메인 페이지 보여주세요 => 메인 페이지를 돌려준다
>
> - 회원가입 페이지 보여주세요 => 회원가입 페이지를 돌려준다
>

요청을 구분하는 2가지

- **url**
- **method**

url과 method의 조합으로 각기 다른 동작을 결정

### 요청하기 - (1) URL과 views 함수 연결하기

모든 요청은 메인 프로젝트 폴더의 `urls.py`로 전달된다고 생각하자!

```python
from django.contrib import admin
from django.urls import path
# articles라는 앱의 views 파이썬 파일을 불러오고
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 불러온 views 파일의 특정 함수를 개발자가 의도한 url이랑 연결
    # ~/index/ 로 접근하면 views의 index 함수가 동작하도록 할거야!
    path('index/', views.index),
]
```

### 요청 처리하기 - (2) views 함수 작성하기

```python
# parameter : request
def index(request):
    # url : ~/index/ 로 접근했을 때
    # 동작하는 함수

    # 어떤 동작? : 렌더하기!
    return render(request, 'index.html')
```

### 요청 처리하기 - (3) template 작성하기

> `index.html`은 `articles`라는 앱의 `templates`라는 폴더 아래에 위치해야한다!!

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>INDEX</h1>
</body>
</html>
```

정리) 기본적인 요청 처리 순서 (uvt)

1. urls - 함수 연결하기
2. views - 함수 작성하기
3. templates - 탬플릿 작성하기 (함수가 탬플릿을 렌더 한다면)


장고 디자인 패턴 (MTV)

1. Model
2. Template
3. View



## Django Template Language

### DTL - Variable : {{ }}

### DTL - Filter : |

### DTL - Tag : {% %}

- for
- if
- extends
- block
- comment
- url : `{% url '별명' %}`  `{% url '앱이름:별명' %}`


## 탬플릿 상속하기


```python
# settings.py

```