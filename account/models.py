from django.db import models

# Create your models here.

class Users(models.Model):
    user_name = models.CharField(max_length=10)
    user_number = models.CharField(max_length=15)
    user_nickName = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=254)
    user_password = models.CharField(max_length=254)
    user_password2 = models.CharField(max_length=254)
    user_tel = models.CharField(max_length=254)


    def __str__(self):
        return self.user_number + " " + self.user_name

class Origin_users(models.Model):
    origin_name = models.CharField(max_length=10)
    origin_number = models.CharField(max_length=15)