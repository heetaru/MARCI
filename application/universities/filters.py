from django import forms
import django_filters
from .models import Faculty, Degree

class FacultyFilter(django_filters.FilterSet):
    degree_type = django_filters.MultipleChoiceFilter(field_name="degrees__type",
                                                      label="Тип освіти",
                                                      choices=Degree.TYPE_CHOICES,
                                                      widget=forms.CheckboxSelectMultiple,)

    class Meta:
        model = Faculty
        fields = []