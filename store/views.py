from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem


def get_cart(request):
    return request.session.get("cart", {})


def productspage(request):
    products = Product.objects.all()
    return render(request, "store/productspage.html", {"products": products})


def productsmoreinfo(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "store/productsmoreinfo.html", {"product": product})


from django.shortcuts import get_object_or_404, redirect
from .models import Product

def addtocart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    try:
        quantity = int(request.POST.get("quantity", 1))
    except ValueError:
        quantity = 1

    if quantity < 1:
        quantity = 1

    cart = request.session.get("cart", {})

    product_id_str = str(product.id)
    current_qty = cart.get(product_id_str, 0)
    cart[product_id_str] = current_qty + quantity

    request.session["cart"] = cart

    return redirect("cartpage")  # or whatever your cart page name is


def removecartitem(request, product_id):
    cart = get_cart(request)
    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session["cart"] = cart
    return redirect("cartpage")


def cartpage(request):
    cart = get_cart(request)
    items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        total += subtotal

        items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal,
        })

    return render(request, "store/cartpage.html", {
        "items": items,
        "total": total,
    })


def checkoutpage(request):
    cart = get_cart(request)

    if not cart:
        return redirect("cartpage")

    items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        total += subtotal

        items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal,
        })

    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        phone_number = request.POST.get("phone_number")

        if customer_name and phone_number:
            order = Order.objects.create(
                customer_name=customer_name,
                phone_number=phone_number
            )

            for item in items:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    quantity=item["quantity"]
                )

            request.session["cart"] = {}

            return render(request, "store/ordersuccess.html", {
                "order": order
            })

    return render(request, "store/checkoutpage.html", {
        "items": items,
        "total": total,
    })