from django import forms
from .models import Question, Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class CommentForm(forms.ModelForm):
    PICK_A = False
    PICK_B = True

    PICKS = [
        (PICK_A, 'BLUE'),
        (PICK_B, 'RED'),
    ]

    pick = forms.ChoiceField(choices=PICKS)
    class Meta:
        model = Comment
        fields = ('pick', 'content', )