from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
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
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
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
        # 유효성 검사
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {
        'form': form
    }
    return render(request, 'articles/new.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    """
    GET : 특정 게시글(pk)을 수정하는 탬플릿을 랜더
    POST : DB에 특정 게시글(pk) 정보 수정
    """
    # 어떤 게시물? pk로 찾기!
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        # POST : DB 특정 게시글 정보 수정
        # ModelForm 클래스로 인스턴스를 생성!
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk)
    else:
        # forms 를 사용! instance에 article 인스턴스를 넘겨준다!
        # 생성된 form 인스턴스에는 article에 대한 정보가 담긴다!
        form = ArticleForm(instance=article)

    context = {
        'form': form
    }
    return render(request, 'articles/edit.html', context)


def delete(request, pk):
    """
    특정 게시물(pk)을 DB에서 삭제
    """
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', pk)