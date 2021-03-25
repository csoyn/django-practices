from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    context = {
        'comment_form': comment_form,
        'article': article
    }
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm()

    context = {
        'article_form': article_form
    }
    return render(request, 'articles/create.html', context)


@require_POST
def comments_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', article_pk)
    context = {
        'comment_form': comment_form,
        'article': article
    }
    return render(request, 'detail.html', context)


@require_POST
def comments_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)

    # comment 인스턴스
    comment = get_object_or_404(Comment, pk=comment_pk)

    # delete()
    comment.delete()
    
    return redirect('articles:detail', article.pk)
    
