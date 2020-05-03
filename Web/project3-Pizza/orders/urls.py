from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("order/<str:name>/<str:option>/<str:size>", views.order, name="order"),
    path("shoppint_cart", views.shoppint_cart, name="shoppint_cart"),
    path("delete/<int:order_nb>", views.delete, name="delete"),
    path("checkout", views.checkout, name="checkout"),
    path("placed", views.placed, name="placed")
]
