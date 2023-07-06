from django.contrib import admin

from main_app.models import *

# Register your models here.
admin.site.register(PostUserModel)
admin.site.register(ProfileUser)
admin.site.register(MessageChat)
admin.site.register(FriendsUsers)