from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def menu(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'platform.html', context)


# def games(request):
#     first = 'Atomic Heart'
#     second = 'Cyberpunk 2077'
#     third = 'PayDay 2'
#     context = {
#         'first': first,
#         'second': second,
#         'third': third
#     }
#     return render(request, 'games.html', context)


def games(request):
    title ='Игры'
    all_games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    buy = 'Купить'
    context = {
        'title': title,
        'all_games': all_games,
        'buy': buy
    }
    return render(request, 'games.html', context)

def cart(request):
    title = 'Корзина'
    text = 'Извините, Ваша корзина пуста'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'cart.html', context)


class Cart(TemplateView):
    template_name = 'cart.html'


