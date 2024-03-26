from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    # slug=forms.slug()
    phone = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                               validators=[validators.MaxValueValidator(11)])
    """phone = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                               validators=[validators.MaxValueValidator(11, 'Way over %(limit_value)s.')])"""
    Password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    # this validation show with error loop in html
    def clean(self):
        cd = super().clean()
        passw = cd["Password"]
        if len(passw) < 8:
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
