from django.db import IntegrityError
import random
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

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


def random_nums():
    num = random.randint(10000000, 99999999)
    return num


def chat_box(request, slug_num):
    if request.user.is_authenticated:
        get_obj_slug = get_object_or_404(MessageChat, slug_num=slug_num)
        if request.method == 'POST':
            form = SearchUser(request.POST)
            if form.is_valid():

                if MessageChat.objects.filter(user1 = request.user.username, user2 = request.POST['username']).first() is None:
                    MessageChat.objects.create(user1 = request.user.username, user2 = request.POST['username'], slug_num=random_nums())
        else:
            form = SearchUser()
        print(get_obj_slug.user1)
        return render(request, "main_app/chat_box.html",
                  {'form_search': form, 'chat_box_ident': get_obj_slug})


def list_chat_box(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SearchUser(request.POST)
            if form.is_valid():

                if MessageChat.objects.filter(Q(user1 = request.user.username) | Q(user2 = request.user.username)).first() is None and request.user.username != request.POST['username']:
                    MessageChat.objects.create(user1 = request.user.username, user2 = request.POST['username'], slug_num=random_nums())
        else:
            form = SearchUser()
        return render(request, "main_app/list_chat_box.html", {'form_search': form, 'list_chat': MessageChat.objects.filter(Q(user1 = request.user.username) | Q(user2 = request.user.username))})

