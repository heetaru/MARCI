from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Users(models.Model):
    user_name = models.TextField("Імʼя користувача")
    user_mail = models.TextField("Пошта користувача")
    user_password = models.TextField("Пароль користувача")