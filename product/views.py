from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, TemplateView,ListView
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

class CategoryStyle(TemplateView):
    template_name = "category.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryStyle, self).get_context_data()
        context["categories"] = Category.objects.all()
        return context


class ProductListview(ListView):
    template_name = "product/product_list.html"
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        request=self.request
        color = request.GET.getlist("color")
        size = request.GET.getlist("size")
        min_price = request.GET.get("min_price")
        max_price = request.GET.get("max_price")
        queryset = Product.objects.all()
        if color:
            queryset=queryset.filter(color__title__in=color).distinct()
        if size:
            queryset = queryset.filter(size__title__in=size).distinct()
        if min_price and max_price:
            queryset = queryset.filter(price__lte=max_price,price__gte=min_price).distinct()

        context = super(ProductListview, self).get_context_data()
        context["object_list"] = queryset
        print(queryset)
        return context



