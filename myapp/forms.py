from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import listingCar, appointment, NewsLetter, testemonial, contactus


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "enter email"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "enter password"
    }))


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "enter username",
        "maxlength": "20",
        "minlength": "4",

    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "enter first name"
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "enter last name"
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "email",
        "placeholder": "enter email"
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "enter password",
        "title": "Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters",
        "pattern": "(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "re-enter password"
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class ListingForm(forms.ModelForm):

    class Meta:
        model = listingCar
        fields = '__all__'


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = appointment
        fields = '__all__'

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields = '__all__'

class testemonialForm(forms.ModelForm):

    class Meta:
        model = testemonial
        fields = '__all__'


class contactusForm(forms.ModelForm):

    class Meta:
        model = contactus
        fields = '__all__'