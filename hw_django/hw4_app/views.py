from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.utils import IntegrityError
from .models import Client, Product, Order
from .forms import ClientForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('show_orders')
        else:
            messages.error(request, 'Логин или пароль неверны')
            return render(request, 'hw4_app/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'hw4_app/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')

            try:
                client = Client(name=name, password=password, email=email, phone_number=phone, address=address)
                client.save()
            except IntegrityError:
                # Обработка ошибки уникального ограничения
                error_message = "Пользователь с таким email уже существует. Выбериите другой"
                return render(request, 'hw4_app/register.html', {'form': form, 'error_message': error_message})

            return redirect('login_view')

    else:
        form = ClientForm()

    return render(request, 'hw4_app/register.html', {'form': form})


def show_orders(request):
    if request.user.is_authenticated:
        current_user = request.user
        client = Client.objects.filter(email=current_user.email).first()

        if not client:
            return HttpResponse('<h3> Пользователь с указанным email не найден </h3>')

        orders = Order.objects.filter(client_id=client.id).all()
        context = {'orders': orders, 'user_id': client.id, 'user_name': client.name}
        return render(request, 'hw4_app/orders_template.html', context)

    return HttpResponse('<h3> Вы не авторизованы </h3>')


def orders_total(request, user_id, interval):
    client = Client.objects.filter(id=user_id).first()
    if not client:
        return HttpResponse('<h3> Пользователь с указанным ID не найден </h3>')

    INTERVALS = {'week': 7, 'month': 30, 'year': 365}
    if interval not in INTERVALS.keys():
        return HttpResponse('<h3> Такого интервала не существует. Выберите week, month или year </h3>')

    orders = Order.orders_by_time_delta(user_id, INTERVALS[interval])
    total_products = Order.get_total_products(orders)
    products = Product.objects.filter(id__in=total_products.keys())

    context = {'orders': orders, 'products' : products, 'total_products':total_products,
               'user_id': user_id, 'user_name': client.name}
    return render(request, 'hw4_app/orders_template.html', context)

