from django.shortcuts import render


# Create your views here.

def index(request):
    context = {'title': 'Главная'}
    return render(request, 'apartaments/index.html', context)

def apartaments(request):
    context = {'title': 'Недвижимость'}
    return render(request, 'apartaments/apartaments.html', context)