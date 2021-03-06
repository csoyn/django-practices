# django model 복습

## Database API

> ORM

### Create

```python
# 1.
article = Article()
article.title = '이거슨 제목'
article.content = '이거슨 내용'
article.save()

# 2.
article = Article(title='이거슨 제목2', content='이거슨 내용2')
article.save()
# save는 반환값이 없다

# 3.
article = Article.objects.create(title='이거슨 제목3', content='이거슨 내용3')
# create는 save가 필요없다! 바로 저장!
# 반환 >>> 새로 생성한 정보가 담겨있는 객체
```

### Read

```python
# 1. 전부 불러오기
articles = Article.objects.all()
print(articles)

# 2. 1개 불러오기
# pk => 고유한 값!
article = Article.objects.get(pk=1)

# 3. 필터링해서 불러오기
articles1 = Article.objects.filter(title='이거슨 제목')
articles2 = Article.objects.filter(pk__gt=2)
# https://docs.djangoproject.com/en/3.1/ref/models/querysets/#field-lookups
```

### Update

```python
# 수정할 대상(객체-정보)이 있어야함!
article = Article.objects.get(pk=1)
article.title = '이거슨 변경된 제목'
article.content = '이거슨 변경된 내용'
article.save() # 까먹지말자!
```

### Delete

```python
# 삭제할 대상(객체-정보)이 있어야함!
article = Article.objects.get(pk=2)
article.delete() # 끝!
```





## 요청 처리하기 - POST

### POST

Database를 조작하는 요청의 경우에 사용하자!!

#### POST는 어떻게 사용할까?

```html
<form method="POST">
</form>
```

##### Django에서는 POST 동작에서 `csrf_token`을 검사한다!

```html
<form method="POST">
  {% csrf_token %}
</form>
```

`csrf_token` : hidden type의 input tag가 생성!


##### POST 주머니

```python
def create(request):
    request.POST.get('name')
```

### GET

정보를 조회하는 경우에 사용하자!!


## 관리자 페이지

```shell
python manage.py createsuperuser
```