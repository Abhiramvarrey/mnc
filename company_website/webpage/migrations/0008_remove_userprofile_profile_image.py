# Generated by Django 4.2.2 on 2023-09-17 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0007_rename_user_userprofile_user_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_image',
        ),
    ]