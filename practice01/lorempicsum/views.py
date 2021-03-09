from django.shortcuts import render


def image(request):
    return render(request, 'lorempicsum/image.html')