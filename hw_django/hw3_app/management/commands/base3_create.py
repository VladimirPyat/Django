import random
from django.utils import timezone

from django.core.management.base import BaseCommand
from hw3_app.models import Client, Product, Order
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **options):
        faker=Faker()
        products = [
            Product(name='headphones', price=5500),
            Product(name='notebook', price=55000),
            Product(name='table', price=11200),
            Product(name='chair', price=2500)
        ]

        for product in products:
            product.save()

        #добавили генерацию произвольных человеческих имен
        clients_num=4
        clients = [Client(name=faker.name()) for _ in range (clients_num)]

        for client in clients:
            client.save()
            self.stdout.write(f'клиент {client.id} создан')
            orders_num = random.randint(0, 5)
            for i in range(orders_num):
                order = Order.objects.create(client=client)
                prod_num = random.randint(1, 3)
                for _ in range(prod_num):
                    product = random.choice(products)
                    order.add_product(product)

                    self.stdout.write(f'к заказу добавлен продукт {product.name} в количестве {product.qty}')
                #меняем дату заказа на произвольную у части заказов
                if i%4 != 0:
                    order.register_date=timezone.make_aware(faker.date_time_this_year())
                order.save()
                self.stdout.write(f'заказ {order.id} создан')


