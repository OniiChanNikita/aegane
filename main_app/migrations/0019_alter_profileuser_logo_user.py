# Generated by Django 3.2.18 on 2023-06-19 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_auto_20230619_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='logo_user',
            field=models.ImageField(blank=True, default='media/default_logo/default_logo.png', upload_to='media/main_app/photo/logo'),
        ),
    ]
