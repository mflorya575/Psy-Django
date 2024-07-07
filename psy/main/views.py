from django.shortcuts import render


def index(request):

    context = {
        'title': 'Главная - Психоаналитика',
    }

    return render(request, 'main/index.html', context)


def about(request):

    context = {
        'title': 'О нас - Психоаналитика',
    }

    return render(request, 'main/about.html', context)
