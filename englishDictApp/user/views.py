from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 

from .form import MyUserCreationForm
from .models import Favorite, Profile


def user_registration(request):
    if request.method == 'GET':
        form = MyUserCreationForm()
        return render(request, 'registration/registration.html', context={'form':form})
    
    form = MyUserCreationForm(request.POST or None)
    print(form)
    if form.is_valid():
        user = form.save()
        login(request, user)    
        return redirect("user:profile")
    
    return render(request, 'registration/registration.html', context={'form':form})
        


@login_required()
def profile_page(request):
    profile = get_object_or_404(Profile, user=request.user)
    words_list = Favorite.objects.filter(user=request.user)
    return render (request, 'profile.html', context={'profile':profile, 'words_list': words_list})