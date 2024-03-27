from django.shortcuts import render, redirect,reverse
from django.views import View
from .forms import LoginForm, RegisterForm,CheckOtpForm
from django.contrib.auth import authenticate, login
from random import randint
from django.contrib.auth.models import User
# Create your views here.
from .models import Otp


class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "account/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd["Password"])
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                form.add_error("phone", "user is not valid")
        else:
            form.add_error("phone", "invalid data")

        return render(request, "account/login.html", {"form": form})


class UserRegister(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "account/rejister.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode=randint(1000,9999)
            print(randcode)
            #you must send sms here
            """"sms.varificatio0n{
                cd["phone"]
            }"""
            Otp.objects.create(phone= cd["phone"],randcode=randcode)
            return redirect(reverse("account:user_checkcode")+ f'?phone={cd["phone"]}')

        else:

            return render(request, "account/rejister.html", {"form": form})



class CheckOtp(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, "account/checkcode.html", {"form": form})

    def post(self, request):
        phone=request.GET.get("phone")
        form = CheckOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print("______")
            print(cd)
            if Otp.objects.filter(randcode=cd["code"],phone=phone).exists():
                user = User.objects.creat_user(phone=phone)
                login(request, user)
                redirect("/")
            else:

                return render(request, "account/checkcode.html", {"form": form,"massage":"user not found"})

        else:

            return render(request, "account/checkcode.html", {"form": form})
