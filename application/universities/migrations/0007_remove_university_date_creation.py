# Generated by Django 5.2 on 2025-04-13 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0006_remove_university_dean_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='date_creation',
        ),
    ]
