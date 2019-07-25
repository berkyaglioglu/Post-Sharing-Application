from django.shortcuts import render, HttpResponseRedirect
from .forms import Register, LoginForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('posts:post_list'))

    form = Register(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse('posts:post_list'))

    return render(request, 'users/register.html', context={'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('posts:post_list'))

    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('posts:post_list'))
        else:
            error = 'Username or Password is Wrong!'
            return render(request, 'users/login.html', context={'form': form, 'error': error})

    return render(request, 'users/login.html', context={'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

