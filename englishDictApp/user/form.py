from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import MyUser, Profile

list
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "register-username", "placeholder":"Username"}),
            "email": forms.TextInput(attrs={"class": "register-email", "placeholder":"Email"}),
            "password1": forms.PasswordInput(attrs={"class": "register-password1"}),
            "password2": forms.PasswordInput(attrs={"class": "register-password2"}),
        }
    

    def save(self, commit = ...):
        user = super().save(commit)
        Profile.objects.create(user=user)
        return user




