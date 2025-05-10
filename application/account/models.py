from django.contrib.auth.models import User
from django.db import models

class Students(models.Model):
    user_name = models.TextField("Імʼя користувача")
    user_mail = models.TextField("Пошта користувача")
    user_password = models.TextField("Пароль користувача")

    def __str__(self):
        return self.user_name

