from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
from .models import Booking


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SigninForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['title', 'description', 'price', 'location']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','subject','message']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date_time', 'destination', 'message']
        widgets = {
            'date_time': forms.TextInput(attrs={
                'class': 'form-control bg-transparent datetimepicker-input',
                'id': 'datetime',
                'placeholder': 'Date & Time',
                'data-target': '#date3',
                'data-toggle': 'datetimepicker'
            }),
            'name': forms.TextInput(attrs={'class': 'form-control bg-transparent'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-transparent'}),
            'destination': forms.Select(attrs={'class': 'form-select bg-transparent'}),
            'message': forms.Textarea(attrs={'class': 'form-control bg-transparent', 'style': 'height: 100px'}),
        }
