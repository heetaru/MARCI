from django.db import models
import datetime
class Faculty(models.Model):
    university_name = models.TextField("Назва університету")
    faculty_name = models.TextField("Назва факультету")
    country = models.TextField("Країна")
    city = models.TextField("Місто")
    mail = models.TextField("Пошта")
    university_description = models.TextField("Опис")


    def __str__(self):
        return self.university_name

    def get_info(self):
        data = {
            'university_name': self.university_name,
            'faculty_name': self.faculty_name,
            'country': self.country,
            'city': self.city,
            'university_description': self.university_description,
            'degrees': [degree.get_info() for degree in self.degrees.all()]
        }
        return data


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
    duration = models.FloatField("Тривалість навчання")
    cost = models.FloatField("Ціна", default=0, blank=True, null=True)
    semester_start = models.DateField("Дата початку семестру", default=datetime.date.today, blank=True, null=True)

    def __str__(self):
        return f"{self.faculty.university_name} || {self.get_type_display()}"

    def get_info(self):
        data = {
            'type': self.get_type_display(),
            'duration': self.duration,
            'cost': self.cost,
        }

        return data

    class Meta:
        verbose_name = 'Ступінь навчання'
        verbose_name_plural = 'Ступені навчання'

class Image(models.Model):
    faculty = models.ForeignKey(Faculty, related_name="images", on_delete=models.CASCADE)
    type = models.TextField("Тип зображення") #main, logo, additional
    image = models.ImageField("Зображення", upload_to="media/", blank=True, null=True)

    class Meta:
        verbose_name = 'Фото університету'
        verbose_name_plural = 'Фото університетів'

