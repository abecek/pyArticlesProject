from pprint import pprint
import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import auth, messages
from django.core import serializers
from . models import Article, Category
from article.forms import RegistrationForm, ChangePasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import json
from datetime import datetime


def get_all_categories():
    results = Category.objects.all()
    return results


def index(request):
    template = 'articles/index.html'
    context = {
        'articles': Article.objects.all(),
        'categories': get_all_categories()
    }

    return render(request, template, context)


'''
def base_layout(request):
    template = 'articles/base.html'
    return render(request, template)
'''


def categories(request):
    template = 'articles/category/all.html'
    context = {
        'categories': get_all_categories()
    }
    return render(request, template, context)


def category_view(request, id_category):
    template = 'articles/category/view.html'
    context = {
        'category': Category.objects.get(pk=id_category),
        'categories': get_all_categories(),
        'articles': Article.objects.all().filter(category_id=id_category).order_by('-created_at')
    }
    return render(request, template, context)


def article_view(request, id_article):
    template = 'articles/article/view.html'
    context = {
        'article': Article.objects.get(pk=id_article),
        'categories': get_all_categories()
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

    context = {
        'categories': get_all_categories()
    }
    return render(request, 'articles/login.html', context)


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

    context = {
        'form': form,
        'categories': get_all_categories()
    }
    return render(request, 'articles/register.html', context)


def change_password(request):
    if not request.user.is_authenticated():
        messages.error(request, '????')
        return redirect('home')

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            # todo
            user.ArticleUser.updated_at = datetime.now()
            user.ArticleUser.save()

            messages.add_message(request, messages.SUCCESS, 'Your password is successfully changed.')
            return redirect('user_details')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form,
        'categories': get_all_categories()
    }
    return render(request, 'articles/changepassword.html', context)


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.SUCCESS, 'You have been logged out.')
    # return render(request, 'articles/logout.html')
    return redirect('home')


def user_details(request):
    if request.user.is_authenticated():
        messages.error(request, '??')
        return redirect('home')

    context = {
        'article_user': request.user.ArticleUser,
        'categories': get_all_categories()
    }
    return render(request, 'articles/user_details.html', context)
