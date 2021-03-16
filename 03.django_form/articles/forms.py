from django import forms
from .models import Article

# form class를 정의
# 1. HTML form tag 생성
# 2. 유효성 검사

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