from django.shortcuts import render
from .forms import UserRegister
from task1.models import Buyer, Goods


def shop(request):
    goods = Goods.objects.all()  # Получаем все продукты из базы данных
    return render(request, 'fourth_task/shop.html', {
        'goods': goods
    })


def get_users():
    users = Buyer.objects.all()  # Получаем всех пользователей
    return users


def main(request):
    dictio = {
        'main': 'Главное меню',
        'shop': 'Магазин',
        'shopping_cart': 'Корзина'
    }
    context = {

        'dictio': dictio,

    }

    return render(request, 'fourth_task/menu.html', context)



def shopping_cart(request):
    dictio = {
        'main': 'Главное меню',
        'shop': 'Магазин',
        'shopping_cart': 'Корзина'
    }
    context = {

        'dictio': dictio,

    }
    return render(request, 'fourth_task/shopping_cart.html', context)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password1 = form.cleaned_data['password1']
            age = form.cleaned_data['age']
            if Buyer.objects.filter(name=username).exists():
                info['error'] = f'Пользователь уже существует'
            elif password != password1:
                info['error'] = f'Пароли не совпадают'
            elif age < 18:
                info['error'] = f'Вы должны быть старше 18'
            else:
                new_buyer = Buyer.objects.create(name=username, balance=100.00, age=age)
                info['success'] = f'Регистрация прошла успешно! Добро пожаловать, {username}!'

        else:
            form = UserRegister()
    print(f'info', info)

    return render(request, 'fourth_task/registration_page.html', info)
