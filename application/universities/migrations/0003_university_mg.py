# Generated by Django 5.2 on 2025-04-12 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0002_alter_university_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='mg',
            field=models.BooleanField(default=False, verbose_name='mg'),
        ),
    ]
