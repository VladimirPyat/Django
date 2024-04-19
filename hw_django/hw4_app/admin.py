from django.contrib import admin
from .models import Client, Order, Product

@admin.action(description="Установить количество=1")
def drop_quantity(modeladmin, request, queryset):
    queryset.update(qty=1)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "description", "price", "qty"]
    actions = [drop_quantity]


admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
