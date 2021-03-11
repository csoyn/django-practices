from django.shortcuts import render
from datetime import datetime

def dtlpractice(request):
    context = {
        'foods': ['김치찌개', '미역국', '라면', '김밥', '스팸', '샌드위치'],
        'fruits': ['apple', 'banana', 'mango'],
        'empty': [],
        'today': datetime.now()
    }
    return render(request, 'dtlpractice/dtlpractice.html', context)
