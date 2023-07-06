from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


TYPE_TRAVEL = (
    ('Domestic Tourism', 'domestic tourism'),
    ('Inbound Tourism', 'inbound tourism'),
    ('Outbound Tourism', 'outbound tourism'),
    ('Leisure Travel', 'leisure travel'),
)


class PostUserModel(models.Model):
    username = models.CharField(max_length=100)
    theme_post = models.CharField(max_length=300)
    content_post = models.TextField()
    country = models.CharField(max_length=50)
    type_travel = models.CharField(max_length=30, choices=TYPE_TRAVEL)
    image_bg_d = models.FileField(upload_to='media/posts/', blank=True, null=True)
    likes = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.theme_post

    def get_absolute_url(self):
        return reverse("slug_name", args=[str(self.id)])


class ProfileUser(models.Model):
    username = models.CharField(max_length=100)
    logo_user = models.ImageField(upload_to='media/logo', blank=True, null=True)
    slug_profile = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    likes_post = models.ManyToManyField(PostUserModel, related_name='likes_post', blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("slug_profile_absolute", args=[str(self.slug_profile)])


class FriendsUsers(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    friends = models.ManyToManyField(User, related_name='user_friends')

    def __str__(self):
        return self.username.username


class MessageChat(models.Model):
    user1 = models.CharField(max_length=215)
    user2 = models.CharField(max_length=215)
    message = models.JSONField(null=True)
    slug_num = models.CharField(max_length=15)
    date_public = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug_num

    def get_absolute_url(self):
        return reverse("chat_detail", args=[str(self.slug_num)])


