from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

TYPE_TRAVEL = (
    ('Domestic Tourism', 'domestic tourism'),
    ('Inbound Tourism', 'inbound tourism'),
    ('Outbound Tourism', 'outbound tourism'),
    ('Leisure Travel', 'leisure travel'),
)


class ProfileUser(models.Model):
    username = models.CharField(max_length=100)
    logo_user = models.ImageField(default='default_logo.png', blank=True, upload_to='static/main_app/photo/logo')

    def __str__(self):
        return self.username


class PostUserModel(models.Model):
    username = models.CharField(max_length=100)
    theme_post = models.CharField(max_length=300)
    content_post = models.TextField()
    country = models.CharField(max_length=50)
    type_travel = models.CharField(max_length=30, choices=TYPE_TRAVEL)
    image_bg_d = models.FileField(upload_to='static/main_app/bg_post/', null=True)

    def __str__(self):
        return self.theme_post

    def get_absolute_url(self):
        return reverse("slug_name", args=[str(self.id)])


class MessageChat(models.Model):
    user1 = models.CharField(max_length=215)
    user2 = models.CharField(max_length=215)
    message = models.JSONField(null=True)
    slug_num = models.CharField(max_length=15)

    def __str__(self):
        return self.slug_num

    def get_absolute_url(self):
        return reverse("chat_detail", args=[str(self.slug_num)])


