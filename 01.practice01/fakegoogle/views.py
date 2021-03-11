from django.shortcuts import render


def fake(request):
    return render(request, 'fakegoogle/fake.html')