from django.urls import path

from . import views

app_name="account"
urlpatterns=[

    path("login",views.UserLogin.as_view(),name="user_login"),
    path("register",views.OtpLoginView.as_view(),name="user_rejister"),
    path("add/address",views.AaaAddressView.as_view(),name="add_address"),
]