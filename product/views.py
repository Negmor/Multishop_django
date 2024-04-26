from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, TemplateView
from product.models import Product, Category
import templates


class ProductDetailView(DetailView):
    template_name = "product/detail.html"
    model = Product


class NavbarPartialView(TemplateView):
    template_name = "navbar.html"

    def get_context_data(self, **kwargs):
        context = super(NavbarPartialView, self).get_context_data()
        context["categories"] = Category.objects.all()
        return context
