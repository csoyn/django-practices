from django.shortcuts import render


def fake(request):
    return render(request, 'fakenaver/fake.html')