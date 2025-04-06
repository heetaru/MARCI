from django.db import models

class University(models.Model):
    name = models.CharField("Назва університету")
    faculty = models.CharField("Назва факультету")
    description = models.TextField("Опис")

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Університет'
        verbose_name_plural = 'Університети'