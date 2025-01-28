from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
def sign_up_by_html(request):
    users = ['Ivan', 'Petr', 'Tina']
    info = {}
    if request.method == 'POST':
        user_exists = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        is_user = username in users
        if is_user:
            info['error'] = 'Пользователь уже существует'
            print(info['error'])
            return HttpResponse(info['error'])
        passwords_matched = password == repeat_password
        if passwords_matched:
            if age >= 18:
                user_exists = True
            else:
                info['error'] = 'Вы должны быть старше 18'
        else:
            info['error'] = 'Пароли не совпадают'

        if user_exists:
            message = f'Приветствуем, {username}!'
        else:
            message = info['error']
        print(message)
        return HttpResponse(message)
    return render(request, 'registration_page.html', info)


# создаем forms.py  в приложении task5
def sign_up_by_django(request):
    users = ['Ivan', 'Petr', 'Tina']
    info = {}
    message = ''
    if request.method == 'POST':
        user_exists = False
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            is_user = username in users
            if is_user:
                info['error'] = 'Пользователь уже существует'
                print(info['error'])
                return HttpResponse(info['error'])
            passwords_matched = password == repeat_password
            if passwords_matched:
                if age >= 18:
                    user_exists = True
                else:
                    info['error'] = 'Вы должны быть старше 18'
            else:
                info['error'] = 'Пароли не совпадают'

            if user_exists:
                message = f'Приветствуем, {username}!'
            else:
                message = info['error']
            print(message)
        return HttpResponse(message)
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'registration_page.html', info)