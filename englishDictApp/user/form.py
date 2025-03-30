from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import MyUser, Profile


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "register-username", "placeholder":"Username"}),
            "email": forms.TextInput(attrs={"class": "register-email", "placeholder":"Email"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm password"
  

    def save(self, commit = ...):
        user = super().save(commit)
        Profile.objects.create(user=user)
        return user




