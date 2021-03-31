from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Comment
from .forms import QuestionForm, CommentForm

def index(request):
    return render(request, 'articles/index.html')


def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = QuestionForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)

    context = {
        'question': question,
        'form': CommentForm()
    }

    return render(request, 'articles/detail.html', context)