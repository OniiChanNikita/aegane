from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", main, name = "main"),
    path("login/", login, name="login"),
    path("signin/", sign_in, name="sign_in"),
    path("logout/", log_out, name="logout"),
    path("profile/", profile, name="profile"),
    path("add_post/", add_post, name="add_post"),
    path("chat/<str:chat_box_name>/", chat_box, name="chat"),
]