from django.urls import path
from . import views

urlpatterns = [
    path("show_orders/", views.show_orders, name="show_orders"),
    path("create_order/", views.create_order, name="create_order"),
    path("delete_order/", views.delete_order, name="delete_order"),
    path("orders_total/<int:user_id>/<str:interval>/", views.orders_total, name="orders_total"),
    path("", views.login_view, name="login_view"),
    path("register/", views.register, name="register"),
]