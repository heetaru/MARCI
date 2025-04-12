from django.db import models

class University(models.Model):
    university_name = models.CharField("Назва університету")
    region = models.TextField("Регіон")
    fakulty_name = models.CharField("Назва факультету")
    rektor_name = models.TextField("ПІБ ректора")
    dean_name = models.TextField("ПІБ декана")
    mail = models.TextField("Пошта")
    date_creation = models.DateField("Дата створення факультету")
    university_description = models.TextField("Опис")
    mg = models.BooleanField("Присутність магістратури", default=False)
    bc = models.BooleanField("Присутність бакалаврату", default=False)

    def str(self):
        return self.university_name

    class Meta:
        verbose_name = 'Університет'
        verbose_name_plural = 'Університети'