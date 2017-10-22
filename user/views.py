from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
from user.forms import SignUpForm, LoginForm


def account_signup(request, **kwargs):
    template = 'user/register.htm'
    if request.method == 'GET':
        return render(request, template)
    elif request.method == 'POST':
        context = {'data': request.POST}
        form = SignUpForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            pswd = form.cleaned_data.get('password1')
            new_user = User.objects.create_user(username=uname, email=email, password=pswd)
            if new_user:
                user = authenticate(username=uname, password=pswd)
                login(request, user)
            return redirect(reverse('home'))
        else:
            context['errors'] = form.errors
            return render(request, template, context)


def account_login(request, **kwargs):
    template = 'user/login.htm'
    if request.method == 'GET':
        return render(request, template)
    elif request.method == 'POST':
        context = {'data': request.POST}
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if 'next' in request.GET:
                        return redirect(request.GET.get('next'))
                    else:
                        return redirect(reverse('home'))
                else:
                    messages.error(request, 'Your account may be deactivated.')
                    return render(request, template, context)
            else:
                messages.error(request, 'Your credentials do not match any record.')
                return render(request, template, context)
        else:
            context['errors'] = form.errors
            return render(request, template, context)


def account_logout(request, **kwargs):
        logout(request)
        return redirect(reverse('home'))
