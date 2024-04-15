from django.core.management import BaseCommand
from hw4_app.models import Product


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