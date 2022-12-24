from django.db import IntegrityError

from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from main_app.forms import InputUserForm
from main_app.models import ProfileUser


def main(request):
    if request.user.is_authenticated:
        profile_logo = '/static/main_app/photo/logo' + ProfileUser.objects.get(username = request.user.username).logo_user.url
        print(profile_logo)
        return render(request, "main_app/main.html", {"profile_logo": profile_logo})
    return render(request, "main_app/main.html")

def login(request):
    if request.user.is_authenticated:
        redirect("main")
    else:
        if request.method == "POST":
            form = InputUserForm(request.POST)
            if form.is_valid():
                username = request.POST["username"]
                password = request.POST["password"]
                user_auth = authenticate(request, username = username, password = password)
                print(user_auth)
                if user_auth is not None:
                    auth_login(request, user_auth)
                    return redirect("main")
        else:
            form = InputUserForm()
        return render(request, "main_app/login.html", {'form': form})

def sign_in(request):
    if request.user.is_authenticated:
        redirect("main")
    else:
        if request.method == "POST":
            form = InputUserForm(request.POST)
            if form.is_valid():
                try:
                    username = request.POST["username"]
                    password = request.POST["password"]
                    User.objects.create_user(username=username, password=password)
                    user_auth = authenticate(request, username=username, password=password)
                    ProfileUser.objects.create(username = username)
                except IntegrityError:
                    return redirect(sign_in)

                if user_auth is not None:
                    auth_login(request, user_auth)
                    return redirect("main")
        else:
            form = InputUserForm()
        return render(request, "main_app/sign_in.html", {"form": form})

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("main")
    return render(request, "main_app/main.html")

def profile(request):
    if request.user.is_authenticated:
        profile_logo = '/static/main_app/photo/logo' + ProfileUser.objects.get(username = request.user.username).logo_user.url
        print(profile_logo)
        return render(request, 'main_app/profile.html', {'profile_logo': profile_logo})  #/static/main_app/photo/logo/default_logo.png
