from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", main, name = "main"),
    path("login/", login, name="login"),
    path("signin/", sign_in, name="sign_in"),
    path("logout/", log_out, name="logout"),
    path("profile/<str:slug_profile>/", profile, name="profile"),
    path("add_post/", add_post, name="add_post"),
    path('chat/', list_chat_box, name='list_chat_box'),
    path('chat/<int:slug_num>/', chat_box, name='chat_box'),
    #path('profile/<str:slug_str>/', profile_users, name='profite_users'),
]