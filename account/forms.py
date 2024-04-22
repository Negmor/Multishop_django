from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from account.models import Address


class LoginForm(forms.Form):
    # slug=forms.slug()
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    """phone = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                               validators=[validators.MaxValueValidator(11, 'Way over %(limit_value)s.')])"""

    Password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    # this validation show with error loop in html
    def clean(self):
        cd = super().clean()
        passw = cd["Password"]
        if len(passw) < 4:
            raise ValidationError('Password is short ')


class ContactForm(forms.Form):
    # Everything as before.
    ...

    def clean_recipients(self):
        data = self.cleaned_data["recipients"]
        if "fred@example.com" not in data:
            raise ValidationError("You have forgotten about Fred!")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data




class OtpLoginForm(forms.Form):
    phone = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    def clean(self):
        cd = super().clean()
        phone= str(cd["phone"])
        print(len(phone))
        if len(phone) < 9:
            raise ValidationError('phone is short ')


class CheckOtpForm(forms.Form):
    code = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))


class AddressCreationForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ('user',)
