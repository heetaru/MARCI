
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='list'),
    path('university-registration/', views.registration, name='registration'),
]
