# Generated by Django 2.1.5 on 2019-05-29 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_password2',
            field=models.CharField(default=' ', max_length=254),
            preserve_default=False,
        ),
    ]
