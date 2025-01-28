from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def platform(request):
    title = 'Platform Games'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'platform.html', context)


def games(request):
    return render(request, 'games.html')


# def cart(request):
#     return render(request, 'cart.html')


class Cart(TemplateView):
    template_name = 'cart.html'



