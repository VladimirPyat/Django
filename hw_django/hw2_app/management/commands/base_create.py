import random
from django.core.management.base import BaseCommand
from hw2_app.models import Client, Product, Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = [
            Product(name='headphones', price=5500),
            Product(name='notebook', price=55000),
            Product(name='table', price=11200),
            Product(name='chair', price=2500)
        ]

        for product in products:
            product.save()
            self.stdout.write('продукт создан')

        clients = [
            Client(name='San Sanych'),
            Client(name='Mary Jane'),
            Client(name='Simon Bolivar')
        ]

        for client in clients:
            client.save()
            self.stdout.write(f'клиент {client.id} создан')
            orders_num = random.randint(0, 3)
            for _ in range(orders_num):
                order = Order.objects.create(client=client)
                prod_num = random.randint(1, 3)
                for _ in range(prod_num):
                    product = random.choice(products)
                    order.add_product(product)

                    self.stdout.write(f'к заказу добавлен продукт {product.name} в количестве {product.qty}')
                order.save()
                self.stdout.write(f'заказ {order.id} создан')


