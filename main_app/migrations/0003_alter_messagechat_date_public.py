# Generated by Django 4.0 on 2023-03-27 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_messagechat_date_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagechat',
            name='date_public',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]