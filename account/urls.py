from django.urls import path

from . import views

app_name="account"
urlpatterns=[

    path("login",views.UserLogin.as_view(),name="user_login"),
    path("register",views.UserRegister.as_view(),name="user_rejister"),
    path("checkcode",views.CheckOtp.as_view(),name="user_checkcode"),
]