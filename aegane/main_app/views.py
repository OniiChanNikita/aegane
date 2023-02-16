from django.db import IntegrityError

from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from main_app.forms import *
from main_app.models import *


def main(request):
    if request.user.is_authenticated:
        profile_logo = '/static/main_app/photo/logo' + ProfileUser.objects.get(
            username=request.user.username).logo_user.url
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
                user_auth = authenticate(request, username=username, password=password)
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
                    ProfileUser.objects.create(username=username)
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
        info_user = ProfileUser.objects.get(username=request.user.username)
        info_user_post = PostUserModel.objects.filter(username=request.user.username)
        profile_logo = '/static/main_app/photo/logo' + info_user.logo_user.url
        print(profile_logo)
        return render(request, 'main_app/profile.html', {'info_user': info_user, 'info_user_post': info_user_post,
                                                         'profile_logo': profile_logo})  # /static/main_app/photo/logo/default_logo.png


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print("aa")
            #form = CreatePostForm(request.POST, request.FILES)
            image_bg = request.FILES['image_bg']

            username_post = request.user.username
            theme_post = request.POST['theme_post']
            content_post = request.POST['content_post']
            country = request.POST['country']
            type_travel = request.POST['type_travel']

            print(image_bg)

            PostUserModel.objects.create(username=username_post, theme_post=theme_post,
                                         content_post=content_post, country=country,
                                         type_travel=type_travel, image_bg=image_bg)
            return redirect("main")
        else:
            print("a")
            form = CreatePostForm()
        return render(request, 'main_app/add_post.html',
                      {'profile': ProfileUser.objects.filter(username=request.user.username), 'form': form})

    return redirect("main")


def chat_box(request, chat_box_name):
    # we will get the chatbox name from the url
    return render(request, "main_app/chatbox.html", {"chat_box_name": chat_box_name})