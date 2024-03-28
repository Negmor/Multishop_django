from django.shortcuts import render, redirect,reverse
from django.views import View
from .forms import LoginForm, RegisterForm,CheckOtpForm
from django.contrib.auth import authenticate, login
from random import randint
from uuid import uuid4
# Create your views here.
from .models import Otp,User
from django.utils.crypto import   get_random_string

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
            token=str(uuid4())
            #you must send sms here
            """"sms.varificatio0n{
                cd["phone"]
            }"""
            Otp.objects.create(phone= cd["phone"],randcode=randcode,token=token)
            return redirect(reverse("account:user_checkcode")+ f'?token={token}')

        else:

            return render(request, "account/rejister.html", {"form": form})



class CheckOtp(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, "account/checkcode.html", {"form": form})

    def post(self, request):
        token = request.GET.get("token")
        form = CheckOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print("______")
            print(cd)
            if Otp.objects.filter(randcode=cd["code"],token=token ).exists():
                otp=Otp.objects.get(token=token)
                user, is_created = User.objects.get_or_create(phone=otp.phone)
                print(user)
                login(request, user)
                otp.delete()
                return redirect("/")
            else:

                return render(request, "account/checkcode.html", {"form": form,"massage":"user not found"})

        else:

            return render(request, "account/checkcode.html", {"form": form})
