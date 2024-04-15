from django.urls import path
from . import views

urlpatterns = [
    path("show_orders/", views.show_orders, name="show_orders"),
    path("orders_total/<int:user_id>/<str:interval>/", views.orders_total, name="orders_total"),
    path("", views.login_view, name="login_view"),
    path("register/", views.register, name="register"),
]