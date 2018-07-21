# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from accounts.forms import RegistraionForm, EditProfileForm, EditUserProfileForm
from django.contrib.auth.models import User
from classifieds.models import Post
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def home(request):
    return render(request, 'accounts/profile.html') # view profile

def register(request):
    if request.method == 'POST':
        form = RegistraionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("login"))
    else:
        form = RegistraionForm()
        args = {'form': form}
        return render(request, 'accounts/register.html', args)

# use login_required decorator to make profile invisable to anonymous users
@login_required
def view_profile(request):
    user_ads = Post.objects.filter(author=request.user).order_by('-pub_date')
    storage = messages.get_messages(request)
    args = {'user': request.user, 'message': storage, 'user_ads': user_ads}
    return render(request, 'accounts/profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your email/name has been updated!")
            return redirect(reverse("view_profile"))

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('/accounts/profile')
    else:
        form = EditUserProfileForm(instance=request.user.userprofile)
        args = {'form': form}
        return render(request, 'accounts/edit_user_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        messages.success(request, "Your password has been updated!")
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

def ad_details(request, ad_id):
    post = get_object_or_404(Post, pk=ad_id)
    args = {'post': post}
    return render(request, 'classifieds/ad-details.html', args)
