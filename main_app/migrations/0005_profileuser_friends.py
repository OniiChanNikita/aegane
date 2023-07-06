# Generated by Django 4.0 on 2023-03-30 15:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0004_alter_postusermodel_image_bg_d'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='friends',
            field=models.ManyToManyField(related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
