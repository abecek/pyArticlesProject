from pprint import pprint
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import auth, messages
from django.core import serializers
from . models import Article
from article.forms import RegistrationForm
import json

'''
def index(request):
    return HttpResponse("Hello Michal!")
'''


def index(request):
    template = 'articles/index.html'
    results = Article.objects.all()
    context = {
        'results': results,
    }

    return render(request, template, context)


'''
def base_layout(request):
    template = 'articles/base.html'
    return render(request, template)
'''


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
    #if request.user.is_authenticated():
     #   messages.error(request, '??')
     #   return redirect('user_details')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your account is successfully created.')
            return redirect('login')
    else:
        form = RegistrationForm()

    args = {'form': form}
    return render(request, 'articles/register.html', args)


def logout(request):
    auth.logout(request)
    #return render(request, 'articles/logout.html')
    messages.add_message(request, messages.SUCCESS, 'You have been logged out.')
    return redirect('home')


def user_details(request):
    #user = get_object_or_404(User, id=request.user.id)
    #return render(request, 'articles/user_details.html', {'user': user})
    return render(request, 'articles/user_details.html', {})
