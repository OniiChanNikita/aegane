import string

from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
import random
import json
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext

from .forms import *
from .models import *


def random_nums():
    num = random.randint(10000000, 99999999)
    return num


def random_str(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def main(request):
    if request.user.is_authenticated:
        profile_slug = ProfileUser.objects.get(username=request.user.username).slug_profile
        profile_logo = ProfileUser.objects.get(
            username=request.user.username).logo_user
        return render(request, "main_app/main.html", {'profile_slug': profile_slug, "profile_logo": profile_logo})
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
                    ProfileUser.objects.update_or_create(username=username, slug_profile=random_str())
                except IntegrityError:
                    print('bad_sign_in')
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


@login_required
def profile(request, slug_profile):
    # friends and post profiles
    get_profile = get_object_or_404(ProfileUser, slug_profile=slug_profile)
    friend_obj, created = FriendsUsers.objects.get_or_create(username=request.user)
    count_friend = friend_obj.friends.all()

    all_posts = list(PostUserModel.objects.all())
    info_user_post = PostUserModel.objects.filter(username=get_profile.username)
    active_profile = ProfileUser.objects.get(username=request.user.username)

    friend = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        if 'button_add_friend' in request.POST:
            print(request.POST)
            if request.user.username != get_profile.username:

                print('add')
                friend_obj.friends.add(friend)
        elif request.is_ajax():
            for post in info_user_post:
                print(request.POST)
                if post.username+'_'+post.theme_post in request.POST:
                    post.likes += 1
                    post.save()
                    active_profile.likes_post.add(post)

    max_likes = PostUserModel.objects.filter(username = get_profile.username).aggregate(max_likes  = models.Max('likes'))

    return render(request, 'main_app/profile.html',
                  {'count_friend': count_friend.count(), 'info_user': get_profile,
                   'info_all_post': random.sample(all_posts, len(all_posts)),
                   'info_user_post': info_user_post,
                   'profile_logo': get_profile.logo_user,
                   'profile_lens': info_user_post.count(),
                   'max_likes': PostUserModel.objects.filter(username = get_profile.username, likes = max_likes['max_likes']).first(),
                   })  # /static/main_app/photo/logo/default_logo.png


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreatePostForm(request.POST, request.FILES)
            if form.is_multipart():
                if 'image_bg' in request.FILES:
                    image_bg = request.FILES['image_bg']
                    file_extension_validator = validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])
                    try:
                        file_extension_validator(image_bg)
                    except validators.ValidationError:
                        return HttpResponse('Недопустимое расширение файла.')
                    username_post = request.user.username
                    theme_post = request.POST['theme_post']
                    content_post = request.POST['content_post']
                    country = request.POST['country']
                    type_travel = request.POST['type_travel']

                    print(image_bg)

                    PostUserModel.objects.create(username=username_post, theme_post=theme_post,
                                                 content_post=content_post, country=country,
                                                 type_travel=type_travel, image_bg_d=image_bg)
                    return redirect("main")
        else:
            print("a")
            form = CreatePostForm()
        return render(request, 'main_app/add_post.html',
                      {'profile': ProfileUser.objects.filter(username=request.user.username), 'form': form})

    return redirect("main")


def chat_box(request, slug_num):
    if request.user.is_authenticated:
        get_obj_slug = get_object_or_404(MessageChat, slug_num=slug_num)
        print(request.user.username, get_obj_slug.user1)
        message_chat = MessageChat.objects.filter(
            Q(user1=request.user.username, user2=get_obj_slug.user2) | Q(user1=get_obj_slug.user1,
                                                                         user2=request.user.username)).first()
        ur_user_logo = ProfileUser.objects.filter(username=request.user.username).first().logo_user
        if get_obj_slug.user1 == request.user.username:
            profile_get_obj_slug = ProfileUser.objects.get(username=get_obj_slug.user2)
            receive_user_logo = ProfileUser.objects.filter(username=get_obj_slug.user2).first().logo_user
        else:
            profile_get_obj_slug = ProfileUser.objects.get(username=get_obj_slug.user1)
            receive_user_logo = ProfileUser.objects.filter(username=get_obj_slug.user1).first().logo_user
        message_dict = list(dict())
        if message_chat is None and request.user.username != request.POST['username']:
            print('so bad')
        if message_chat.message is not None and message_chat.message != 'null':
            for messages in message_chat.message:
                message_dict.append({messages['username']: messages['message'], })

        print('message_dict--->', message_dict)

        # --------------
        message_list = []
        for i in message_dict:
            message_list.append(i)
        print('message_list--->', message_list)
        # --------------
        num = 0

        if request.method == 'POST':
            form = SearchUser(request.POST)
            if form.is_valid():

                if request.user.username != request.POST['username']:
                    MessageChat.objects.create(user1=request.user.username, user2=request.POST['username'],
                                               slug_num=random_nums())
        else:
            form = SearchUser()
        return render(request, "main_app/chat_box.html",
                      {'form_search': form, 'list_chat': MessageChat.objects.filter(
                          Q(user1=request.user.username) | Q(user2=request.user.username)),
                       'chat_box_ident': get_obj_slug, 'profile_get_obj_slug':profile_get_obj_slug,
                       'message_dict': message_dict,
                       'message_dict_json': message_chat.message, 'ur_user_logo': ur_user_logo,
                       'receive_user_logo': receive_user_logo})
    else:
        return redirect("main")


def list_chat_box(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SearchUser(request.POST)
            if form.is_valid():

                if request.user.username != request.POST['username']:
                    MessageChat.objects.create(user1=request.user.username, user2=request.POST['username'],
                                               slug_num=random_nums())
        else:
            form = SearchUser()
        return render(request, "main_app/list_chat_box.html", {'form_search': form,
                                                               'list_chat': MessageChat.objects.filter(
                                                                   Q(user1=request.user.username) | Q(
                                                                       user2=request.user.username))})
