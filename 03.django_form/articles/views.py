from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def index(request):
    """
    모든 게시물을 보여주는 탬플릿을 랜더하는 함수
    """
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    """
    특정 게시물(pk)의 상세 내용을 보여주는 탬플릿을 랜더하는 함수
    """
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def create(request):
    """
    GET : 새 게시글을 작성하는 탬플릿을 랜더
    POST : DB에 새 게시글 정보 저장(생성)
    """
    # url은 하나만 쓰고
    # method로 동작을 구분!

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        return redirect('articles:create')
    else:
        form = ArticleForm()
        context = {
            'form': form
        }
        return render(request, 'articles/new.html', context)

    