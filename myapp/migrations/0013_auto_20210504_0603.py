# Generated by Django 3.1.2 on 2021-05-04 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='useremail',
            new_name='useremails',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='username',
            new_name='usernames',
        ),
    ]
