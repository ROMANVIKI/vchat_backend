# Generated by Django 4.2.7 on 2023-11-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0005_alter_user_avatar_alter_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(max_length=500, null=True),
        ),
    ]