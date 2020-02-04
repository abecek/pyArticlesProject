from pprint import pprint
import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import auth, messages
from django.core import serializers
from . models import Article
from article.forms import RegistrationForm, ChangePasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import json
import os
from datetime import datetime

'''
def index(request):
    return HttpResponse("Hello Michal!")
'''


def index(request):
    template = 'articles/index.html'
    results = Article.objects.all()
    context = {
        'articles': results,
    }

    return render(request, template, context)


'''
def base_layout(request):
    template = 'articles/base.html'
    return render(request, template)
'''


def article_view(request, id_article):
    template = 'articles/article/view.html'
    result = Article.objects.get(pk=id_article)
    context = {
        'article': result,
    }

    return render(request, template, context)


def login(request):
    if request.user.is_authenticated():
        messages.error(request, '??')
        return redirect('user_details')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'You have been properly logged in.')
            return redirect('user_details')
        else:
            messages.error(request, 'Error: wrong username or password')

    return render(request, 'articles/login.html')


def register(request):
    if request.user.is_authenticated():
        messages.error(request, '?????')
        return redirect('home')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.add_message(request, messages.SUCCESS, 'Your account is successfully created.')
            return redirect('login')
    else:
        form = RegistrationForm()

    args = {'form': form}
    return render(request, 'articles/register.html', args)


def change_password(request):
    #if not request.user.is_authenticated():
     #   messages.error(request, '????')
     #   return redirect('home')

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            # todo
            #user.ArticleUser.updated_at = datetime.now()
            messages.add_message(request, messages.SUCCESS, 'Your password is successfully changed.')
            return redirect('user_details')
    else:
        form = PasswordChangeForm(request.user)

    args = {'form': form}
    return render(request, 'articles/changepassword.html', args)


def logout(request):
    auth.logout(request)
    #return render(request, 'articles/logout.html')
    messages.add_message(request, messages.SUCCESS, 'You have been logged out.')
    return redirect('home')


def user_details(request):
    #user = get_object_or_404(User, id=request.user.id)
    #return render(request, 'articles/user_details.html', {'user': user})
    return render(request, 'articles/user_details.html', {})
