from django.urls import path

from . import views

app_name="cart"
urlpatterns=[

    path("detail",views.CartDtailView.as_view(),name="cart_detail"),
    path("Add/<int:pk>",views.CartAddView.as_view(),name="cart_add"),

]