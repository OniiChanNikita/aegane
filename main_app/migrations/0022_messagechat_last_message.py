# Generated by Django 4.2.3 on 2023-07-20 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_auto_20230620_0555'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagechat',
            name='last_message',
            field=models.TextField(blank=True),
        ),
    ]