
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='list'),
    path('fakulty-registration/', views.fakulty_registration, name='registration'),
    path('fakulty-registration/degree/', views.fakulty_registration_degree, name='fakulty-registration-degree'),
    path('fakulty/<int:pk>', views.UniversityView.as_view(), name='university_view'),
]
