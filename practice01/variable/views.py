from django.shortcuts import render


# 가변인자 => 파라미터(2번째 부터)
def introduce(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'variable/introduce.html', context)


def times(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'result': num1 * num2,
    }
    return render(request, 'variable/times.html', context)


def area(request, r):
    context = {
        'r': r,
        'result': r * r * 3.14,
    }
    return render(request, 'variable/area.html', context)