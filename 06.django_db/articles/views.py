from django.shortcuts import render, get_object_or_404
from .models import Article

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'detail.html', context)