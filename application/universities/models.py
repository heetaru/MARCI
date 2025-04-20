from django.db import models

class Faculty(models.Model):
    university_name = models.CharField("Назва університету")
    fakulty_name = models.CharField("Назва факультету")
    country = models.TextField("Країна")
    city = models.TextField("Місто")
    mail = models.TextField("Пошта")
    university_description = models.TextField("Опис")


    def str(self):
        return self.university_name

    class Meta:
        verbose_name = 'Університет'
        verbose_name_plural = 'Університети'

class Degree(models.Model):
    TYPE_CHOICES = [
        (0, 'Молодший бакалавр'),
        (1, 'Бакалавр'),
        (2, 'Магістр'),
        (3, 'Доктор філософії'),
        (4, 'Доктор наук'),
    ]

    faculty = models.ForeignKey(Faculty, related_name="degrees", on_delete=models.CASCADE)
    type = models.IntegerField("Айді ступеня освіти", choices=TYPE_CHOICES)
    duration = models.IntegerField("Тривалість навчання")
    cost = models.FloatField("Ціна")

class Image(models.Model):
    faculty = models.ForeignKey(Faculty, related_name="images", on_delete=models.CASCADE)
    type = models.TextField("Тип зображення") #main, logo, additional
    image = models.ImageField("Зображення", upload_to="media/")