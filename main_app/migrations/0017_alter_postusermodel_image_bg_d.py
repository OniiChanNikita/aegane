# Generated by Django 3.2.18 on 2023-06-19 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20230401_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postusermodel',
            name='image_bg_d',
            field=models.FileField(default='default_post.jpg', upload_to='static/main_app/photo/photo_post'),
        ),
    ]
