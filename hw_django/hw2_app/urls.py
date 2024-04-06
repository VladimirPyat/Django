from django.urls import path
from . import views

urlpatterns = [
    path("show_orders/<int:user_id>/", views.show_orders, name="show_orders"),
]