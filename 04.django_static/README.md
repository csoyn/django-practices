# Django Form

## 정의

```python
# articles/forms.py

from django import forms
from .models import Article

# form class 특징
# 1. HTML form tag 생성
# 2. 유효성 검사(ModelForm)

# Form
# class ArticleForm(forms.Form):
#     REGIONS = [
#         ('seoul', '서울'),
#         ('daejeon', '대전'),
#         ('gwangju', '광주'),
#         ('gumi', '구미'),
#     ]
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     # 실제 모델과는 관련 없는 필드도 form 요소로 구성 가능하다
#     region = forms.ChoiceField(choices=REGIONS, widget=forms.RadioSelect)



# ModelForm : 이미 정의한 Model과 연관있는 Form
class ArticleForm(forms.ModelForm):
    class Meta:
        # Model 연결
        model = Article
        # fields = ('title', )
        # exclude = ('content', )
        fields = '__all__'
```

## 사용

### `views.py`

#### GET : Template 랜더

```python
form = ArticleForm()
context = {
    'form': form
}
return render(request, 'articles/new.html', context)
```

#### POST : DB에 정보 생성

```python
form = ArticleForm(request.POST)
if form.is_valid():
    article = form.save()
    return redirect('articles:detail', article.pk)
```

### `templates`

```HTML
<form method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <button>제출</button>
</form>
```


## 코드 개선하기

### new & create 로직 변경

**url은 하나만 쓰고 method로 동작을 구분!**

```python
def create(request):
    """
    GET : 새 게시글을 작성하는 탬플릿을 랜더
    POST : DB에 새 게시글 정보 저장(생성)
    """
    if request.method == 'POST':
        # request.POST 정보가 들어가있는 form 인스턴스를 생성
        form = ArticleForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            # 검사를 통과하면 저장
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # ModelForm Class로 form 인스턴스를 생성
        form = ArticleForm()

    # 탬플릿을 랜더 (유효성 검사를 통과하지 못한 경우)
    # 유효성 검사에서 사용한 form 인스턴스를 재사용하기 때문에
    # 유효성 검사를 통과하지 못했을때 기존 내용을 보존할 수 있다!
    context = {
        'form': form
    }
    return render(request, 'articles/new.html', context)

```


### edit & update 로직 변경

```python
def update(request, pk):
    """
    GET : 특정 게시글(pk)을 수정하는 탬플릿을 랜더
    POST : DB에 특정 게시글(pk) 정보 수정
    """
    # pk에 해당하는 정보가 있으면 object를 반환
    # 없으면 404 page로 이동
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        # ModelForm 클래스로 인스턴스를 생성!
        # 1. 사용자로부터 입력 받은 정보 : request.POST
        # 2. 기존 인스턴스 : instance=article
        form = ArticleForm(request.POST, instance=article)

        # 유효성 검사
        if form.is_valid():
            # 검사 통과하면 수정을 반영
            form.save()
            return redirect('articles:detail', pk)
    else:
        # forms 를 사용! instance에 article 인스턴스를 넘겨준다!
        # 생성된 form 인스턴스에는 article에 대한 정보가 담긴다!
        form = ArticleForm(instance=article)

    # 탬플릿을 랜더
    # 유효성 검사를 통과하지 못 했을 때,
    # 유효성검사에서 사용한 form 인스턴스가 재사용됨!
    context = {
        'form': form
    }
    return render(request, 'articles/edit.html', context)
```