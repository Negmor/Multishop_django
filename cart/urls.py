from django.urls import path

from . import views

app_name="cart"
urlpatterns=[

    path("detail",views.CartDtailView.as_view(),name="cart_detail"),
    path("Add/<int:pk>",views.CartAddView.as_view(),name="cart_add"),
    path("delete/<str:id>",views.CartDeleteView.as_view(),name="cart_delete"),
    path("order/<int:pk>",views.OrderDetailView.as_view(),name="order_detail"),
    path("order/creat",views.OrderCreationView.as_view(),name="order_creation"),
    path("order/discount/<int:pk>",views.ApplyDiscountView.as_view(),name="discount_code"),

]