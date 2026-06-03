from django.urls import path
from . import views

urlpatterns = [
    path("", views.productspage, name="productspage"),
    path("products/<int:product_id>/", views.productsmoreinfo, name="productsmoreinfo"),
    path("add-to-cart/<int:product_id>/", views.addtocart, name="addtocart"),
    path("cart/", views.cartpage, name="cartpage"),
    path("remove-from-cart/<int:product_id>/", views.removecartitem, name="removecartitem"),
    path("checkout/", views.checkoutpage, name="checkoutpage"),
]