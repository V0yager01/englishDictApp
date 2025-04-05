from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.tokens import default_token_generator

from .form import MyUserCreationForm
from .tasks import email_verification
from .utils import generate_url, get_user_by_uidb
from .models import Favorite, Profile


def user_registration(request):
    form = MyUserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        email = form.cleaned_data['email']
        link = generate_url(request, user)
        email_verification.delay(link=link, recipient_list=[email])   
        return render(request, 'registration/email_verify_page.html', context={'email':email})
    return render(request, 'registration/registration.html', context={'form':form})
        

@login_required()
def profile_page(request):
    profile = get_object_or_404(Profile, user=request.user)
    words_list = Favorite.objects.filter(user=request.user)
    return render(request, 'profile.html', context={'profile':profile, 'words_list': words_list})


def email_verify(request, uidb64, token):
    try:
        user = get_user_by_uidb(uidb64)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
        return redirect('user:profile')
    except Exception:
        return redirect('user:signup')
    
