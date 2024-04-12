
from django.core.validators import MinValueValidator
from django.db import models


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

    def add_product(self, product):
        if product in self.products.all():
            ordered_product = self.products.get(pk=product.pk)
            ordered_product.qty += product.qty
            ordered_product.save()
        else:
            self.products.add(product)

        self.total_price += product.price
        return

    def __str__(self):
        products_list = self.products.all()
        product_str = ', '.join(f'{product.name} - {product.qty}' for product in products_list)

        return f'{self.pk} ({product_str})'



