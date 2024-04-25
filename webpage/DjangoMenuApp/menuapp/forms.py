from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MenuItem

class RegisterForm(UserCreationForm):
    is_admin = forms.BooleanField(required=False)

class LoginForm(AuthenticationForm):
    pass

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['title', 'description', 'price']
