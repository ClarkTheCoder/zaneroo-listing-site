# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import PostForm
from .models import Post

# Create your views here.

def latest_ads(request):
    storage = messages.get_messages(request)
    posts = Post.objects.order_by('-pub_date')
    args = {'message': storage, 'posts': posts}
    return render(request, 'classifieds/latest-ads.html', args)

@login_required
def create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        messages.success(request, "Your ad has been posted!")
        return redirect(reverse('classifieds:latest_ads'))
    else:
        form = PostForm()
        args = {'form': form}
        return render(request, 'classifieds/create-post.html', args)

def ad_details(request, ad_id):
    post = get_object_or_404(Post, pk=ad_id)
    args = {'post': post}
    return render(request, 'classifieds/ad-details.html', args)















