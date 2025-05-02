from django import forms
import django_filters
from .models import Faculty, Degree

def get_country_choices():
    # Повертає список кортежів (country, country), наприклад: [('Україна', 'Україна'), ('Польща', 'Польща')]
    return [(c["country"], c["country"]) for c in Faculty.objects.values("country").distinct()]

class FacultyFilter(django_filters.FilterSet):
    degree_type = django_filters.MultipleChoiceFilter(
        field_name="degrees__type",
        label="Ступінь освіти",
        choices=Degree.TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )

    faculty_country = django_filters.MultipleChoiceFilter(
        field_name="country",
        label="Країна",
        choices=get_country_choices,  # <- не виконується одразу, а тільки коли потрібно
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Faculty
        fields = ["degree_type", "faculty_country"]