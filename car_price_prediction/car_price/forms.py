from django import forms
from .models import CarPrice
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CarPriceForm(forms.ModelForm):
    class Meta:
        model =CarPrice
        exclude = ['price']


class SignUpForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
         
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['username'].label = False
        self.fields['username'].widget.attrs.update({'placeholder':'Username'})
        self.fields['password1'].help_text = ''
        self.fields['password1'].label = False
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter Password'})
        self.fields['password2'].help_text = ''
        self.fields['password2'].label = False
        self.fields['password2'].widget.attrs.update({'placeholder': 'Repeat Password'})

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput)
  