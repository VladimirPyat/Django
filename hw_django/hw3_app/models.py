
from django.core.validators import MinValueValidator
from django.db import models

from datetime import timedelta
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    register_date = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=150)
    price = models.FloatField(blank=False)
    qty = models.IntegerField(validators=[MinValueValidator(0)], default=1)
    register_date = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)
    products = models.ManyToManyField(Product)
    total_price = models.FloatField(default=0)
    register_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def orders_by_time_delta(cls, user_id, days):
        time_delta = timedelta(days=days)
        today = timezone.now().date()
        orders = Order.objects.filter(register_date__date__range=[today - time_delta, today], client_id=user_id)
        return orders

    def add_product(self, product):
        if product in self.products.all():
            existing_product = self.products.get(pk=product.pk)
            existing_product.qty += product.qty
            existing_product.save()
        else:
            self.products.add(product)

        self.total_price += product.price
        return

    @staticmethod
    def get_total_products(orders):
        #возвращаем словарь содержащий id продукта и его общее количество в списке заказов
        total_products = {}
        for order in orders:
            for product in order.products.all():
                total_products[product.id] = total_products.setdefault(product.id, 0)+product.qty

        return total_products




    def __str__(self):
        products_list = self.products.all()
        result = []
        for product in products_list:
            product_info = {
                'id': product.id,
                'name': product.name,
                'qty': product.qty
            }
            products_list.append(product_info)

        return result



