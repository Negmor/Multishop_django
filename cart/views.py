from django.shortcuts import render,redirect
from django.views import View


# Create your views here.
class CartDtailView(View):
    def get(self, request):
        return render(request, "cart/cart.html")


class CartAddView(View):
    def post(self,request):
        print("add")
        return redirect("cart:cart_detail")
