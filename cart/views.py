from django.shortcuts import render, redirect, get_list_or_404
from django.views import View
from .cart_module import Cart

# Create your views here.
from product.models import Product
from .models import Order, OrderItem


class CartDtailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, "cart/cart.html", {"cart": cart})


class CartAddView(View):
    def post(self, request, pk):
        product = Product.objects.get(id=pk)
        size, color, quantity = request.POST.get("size"), request.POST.get("color"), request.POST.get("quantity")
        cart = Cart(request)
        cart.add(product, size, color, quantity)
        return redirect("cart:cart_detail")


class CartDeleteView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect("cart:cart_detail")


class OrderDetailView(View):
    def get(self,request,pk):
        order = Order.objects.get(id=pk)
        return render(request, "cart/order_detail.html",{"order":order})


class OrderCreationView(View):
    def get(self, request):
        cart=Cart(request)
        order=Order.objects.create(user=request.user,total=cart.total())
        for item in cart:
            OrderItem.objects.create(order=order,product=item["product"],color=item["color"],size=item["size"]
                                     ,quantity=item["quantity"],price=item["price"])
        return redirect("cart:order_detail",order.id)

