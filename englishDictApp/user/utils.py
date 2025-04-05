from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.shortcuts import HttpResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from .models import MyUser


def generate_url(request, user):
    uid, token = urlsafe_base64_encode(force_bytes(user.pk)), default_token_generator.make_token(user)
    verification_link = request.build_absolute_uri(reverse("user:email_verify", args=[uid, token]))
    return verification_link


def get_user_by_uidb(uidb64):
    uid = urlsafe_base64_decode(uidb64).decode()
    user = MyUser.objects.get(pk=uid)
    return user