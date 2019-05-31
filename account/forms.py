from django.contrib.auth.models import User
from django import forms
from .models import Profile
from betterforms.multiform import MultiForm
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','num','tel',]

class UserCreationMultiForm(MultiForm):
    form_classes = {
        'user':UserCreationForm,
        'profile':ProfileForm,
    }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']