from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import LoginForm, OtpLoginForm, CheckOtpForm, AddressCreationForm
from django.contrib.auth import authenticate, login
from random import randint
from uuid import uuid4
# Create your views here.
from .models import Otp, User
from django.utils.crypto import get_random_string


class UserLogin(View):
    form = LoginForm()

    def get(self, request):
        form = LoginForm()
        return render(request, "account/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd["Password"])
            print(user)
            if user is not None:
                login(request, user)
                next_page=request.GET.get("next")
                if next_page:
                    return redirect(next_page)
                return redirect("/")
            else:
                form.add_error("username", "user is not valid")
        else:
            form.add_error("username", "invalid data")

        return render(request, "account/login.html", {"form": form})


class OtpLoginView(View):
    form = OtpLoginForm()

    def get(self, request):
        form = OtpLoginForm()
        return render(request, "account/rejister.html", {"form": form})

    def post(self, request):
        form = OtpLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000, 9999)
            print(randcode)
            token = str(uuid4())
            # you must send sms here
            """"sms.varificatio0n{
                cd["phone"]
            }"""
            Otp.objects.create(phone=cd["phone"], randcode=randcode, token=token)
            return redirect(reverse("account:user_checkcode") + f'?token={token}')

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
            if Otp.objects.filter(randcode=cd["code"], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, is_created = User.objects.get_or_create(phone=otp.phone)
                # user.backend="django.contrib.auth.backends.ModelBackend"
                print(user)
                login(request, user, backend="django.contrib.auth.backends.ModelBackend")
                otp.delete()
                return redirect("/")
            else:

                return render(request, "account/checkcode.html", {"form": form, "massage": "user not found"})

        else:

            return render(request, "account/checkcode.html", {"form": form})


class AddAddressView(View):
    def post(self, request):
        form = AddressCreationForm(request.POST)
        if form.is_valid():
            address=form.save(commit=False)
            address.user= request.user
            address.save()
            next_page=request.GET.get("next")
            if next_page:
                return redirect(next_page)
        return render(request, "account/add_address.html", {"form": form})

    def get(self, request):
        form = AddressCreationForm()
        return render(request, "account/add_address.html", {"form": form})
