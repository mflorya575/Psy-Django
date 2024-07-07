from django.shortcuts import render


def index(request):

    context = {
        'title': 'Главная - Психоаналитика',
    }

    return render(request, 'main/index.html', context)
