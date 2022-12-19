from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", main, name = "main"),
    path("login/", login, name="login"),
    path("signin/", sign_in, name="sign_in"),
    path("logout/", log_out, name="logout"),
    path("profile/", profile, name="profile")
]
