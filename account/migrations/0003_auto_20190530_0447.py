# Generated by Django 2.1.5 on 2019-05-29 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_users_user_password2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user_id',
        ),
        migrations.AddField(
            model_name='users',
            name='user_nickname',
            field=models.CharField(default=' ', max_length=10),
            preserve_default=False,
        ),
    ]