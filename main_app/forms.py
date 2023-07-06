from django import forms
from .models import TYPE_TRAVEL
from django.core import validators

class InputUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CreatePostForm(forms.Form):
    username_post = forms.CharField()
    theme_post = forms.CharField(max_length=300)
    content_post = forms.CharField(widget=forms.Textarea(attrs={}))
    country = forms.CharField(max_length=30, label="country")
    type_travel = forms.ChoiceField(choices=TYPE_TRAVEL, label="type_travel")
    image_bg = forms.ImageField(validators=[validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])


class SearchUser(forms.Form):
    username = forms.CharField(max_length=255)
