from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm



def index(request):
    articles = Article.objects.order_by('-pk')

    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


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
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
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
        comment.user = request.user
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
    

def likes(request, article_pk):
    # 로그인한 사람인지 확인
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    article = get_object_or_404(Article, pk=article_pk)

    # article에 좋아요를 누른 상태인지 판단
    # 1. in : 좋아요 버튼을 누른 사람 article.like_users에 있는가?
    # if request.user in article.like_users.all():

    # 2. exists : article.like_users에 현재 유저의 pk를 가진 정보가 있는가?
    if article.like_users.filter(pk=request.user.pk).exists():
        # 좋아요 취소
        article.like_users.remove(request.user)
    else:
        # 좋아요
        article.like_users.add(request.user)

    return redirect('articles:detail', article_pk)