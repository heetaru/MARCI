
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='list'),
    path('fakulty-registration/', views.registration, name='registration'),
    path('fakulty-registration/images', views.fakulty_registration_images, name='fakulty-registration-image'),
    path('university/<int:pk>', views.UniversityView.as_view(), name='university_view'),
]
