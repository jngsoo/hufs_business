from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    num = models.CharField(max_length=15)
    tel = models.CharField(max_length=20)


class Origin_users(models.Model):
    origin_name = models.CharField(max_length = 15)
    origin_num = models.CharField(max_length=15)