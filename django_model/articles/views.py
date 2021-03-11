from django.shortcuts import render, redirect
from .models import Article

# READ - all
def index(request):
    # articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-pk')

    # for article in articles:
    #     print(article.title)

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# READ - get
def detail(request, pk):
    # 필요한 정보! => pk! => variable routing
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


# CREATE (new & create)
def new(request):
    return render(request, 'articles/new.html')


def create(request):
    '''
    form에서 넘어온 데이터를 DB에 반영 (생성)
    '''
    # Database 조작 => GET X : GET은 데이터 조회
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    #1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2. 
    article = Article(title=title, content=content)
    article.save()

    #3.
    # Article.objects.create(title=title, content=content)

    # 굳이? 새로운 html을 랜더해야할까?
    # return render(request, 'articles/create.html')
    # 그냥 게시판으로 이동시켜주자!
    return redirect('articles:index')


# UPDATE (edit & update)
def edit(request, pk):
    '''
    게시물 수정하는 페이지를 랜더하는 함수
    => 수정하는 페이지에서 기존에 작성된 게시물 내용(article)을 보여준다!
    '''
    # 어떤 게시물 수정할래? => pk!
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)
    

def update(request, pk):
    '''
    form에서 넘어온 데이터를 DB에 반영 (수정)
    '''
    article = Article.objects.get(pk=pk)

    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content
    article.save()
    # 굳이 update라는 탬플릿을 랜더할 필요가 있을까?
    # return render(request, 'articles/update.html')

    # 그냥 해당 게시물을 다시 보여준다!
    return redirect('articles:detail', article.pk)


# DELETE
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', pk)