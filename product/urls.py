
from django.urls import path
from . import views


app_name ="detail"
urlpatterns = [

  path("<int:pk>",views.ProductDetailView.as_view(),name="product_dtail"),
  path("navbar",views.NavbarPartialView.as_view(),name="navbar"),
  path("category",views.CategoryStyle.as_view(),name="category")
]
