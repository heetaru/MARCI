
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='list'),
    path('fakulty-registration/', views.fakulty_registration, name='registration'),
    path('fakulty-registration/degree/', views.fakulty_registration_degree, name='fakulty-registration-degree'),
    path('fakulty-registration/images/', views.fakulty_registration_images, name='fakulty-registration-images'),
    path('fakulty/<int:pk>', views.UniversityView.as_view(), name='university_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

