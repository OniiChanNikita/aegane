# Generated by Django 4.2.3 on 2023-07-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0023_alter_messagechat_last_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagechat',
            name='last_username',
            field=models.CharField(blank=True, max_length=215, null=True),
        ),
    ]