# Generated by Django 2.1.5 on 2019-05-29 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_origin_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_password2',
            field=models.CharField(default=0, max_length=254),
            preserve_default=False,
        ),
    ]
