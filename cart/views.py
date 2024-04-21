from django.shortcuts import render,redirect,get_list_or_404
from django.views import View


# Create your views here.
from product.models import Product


class CartDtailView(View):
    def get(self, request):
        return render(request, "cart/cart.html")


class CartAddView(View):
    def post(self,request,pk):
        product=get_list_or_404(Product,id=pk)
        size,color,quantity=request.POST.get("size"),request.POST.get("color"),request.POST.get("quantity")
        print(size,color,quantity)
        return redirect("cart:cart_detail")
