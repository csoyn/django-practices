from django.shortcuts import render

def dtlpractice(request):
    context = {
        'foods': ['김치찌개', '미역국', '라면', '김밥', '스팸', '샌드위치'],
        'fruits': ['apple', 'banana', 'mango'],
        'empty': [],
    }
    return render(request, 'dtlpractice/dtlpractice.html', context)
