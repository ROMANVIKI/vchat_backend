# Generated by Django 4.2.7 on 2023-11-22 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0003_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=False, upload_to=''),
        ),
    ]
