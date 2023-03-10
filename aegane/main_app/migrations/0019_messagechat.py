# Generated by Django 4.0 on 2023-02-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_delete_messagechat'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.CharField(max_length=215)),
                ('user2', models.CharField(max_length=215)),
                ('message', models.JSONField(null=True)),
                ('slug_num', models.CharField(max_length=15)),
            ],
        ),
    ]
