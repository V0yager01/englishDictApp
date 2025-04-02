from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser, Profile


class MyUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.TextInput(attrs={"placeholder":"Password"}))
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.TextInput(attrs={"placeholder":"Confirm password"}))
    class Meta:
        model = MyUser
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "register-username", "placeholder":"Username"}),
            "email": forms.TextInput(attrs={"class": "register-email", "placeholder":"Email"}),
        }
     

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
  

    def save(self, commit = ...):
        user = super().save(commit)
        Profile.objects.create(user=user)
        return user




