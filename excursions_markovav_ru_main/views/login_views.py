from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from excursions_markovav_ru_main.forms import PassLoginForm
from excursions_markovav_ru_main.views.utils import get_base_context


def login_page(request):
    if request.method == 'POST':
        login_form = PassLoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.data['username']
            password = login_form.data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Авторизация успешна")
                print("Successful auth:", username)
            else:
                messages.add_message(request, messages.ERROR, "Неправильный логин или пароль")
        else:
            messages.add_message(request, messages.ERROR, "Некорректные данные в форме авторизации")
    else:
        context = get_base_context(request)
        context['loginform'] = PassLoginForm()
        return render(request, 'pages/authorizate/login.html', context)
    return redirect('index')


def logout_page(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Вы успешно вышли из аккаунта")
    return redirect('index')
