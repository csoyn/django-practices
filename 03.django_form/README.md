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
return redirect('articles:create')
```

### `templates`

```HTML
<form method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <button>제출</button>
</form>
```