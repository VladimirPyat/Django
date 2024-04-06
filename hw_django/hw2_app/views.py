from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Product, Order


def show_orders(request, user_id):
    client = Client.objects.filter(id=user_id).first()
    if not client:
        return HttpResponse('<h3> Пользователь с указанным ID не найден </h3>')
    orders = Order.objects.filter(client_id=user_id).all()
    orders_str = f'<h3>Заказы пользователя: {user_id} </h3>'

    for order in orders:
        orders_str += f'<h4>Заказ номер {order.id}: </h4>'

        for product in order.products.all():
            orders_str += f'{product.name} - {product.qty} шт.<br>'

    return HttpResponse(orders_str)

