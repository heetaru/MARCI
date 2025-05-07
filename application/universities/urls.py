
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='list'),
    path('accounts/', include('accounts.urls')),
    path('faculty-registration/', views.faculty_registration, name='registration'),
    path('faculty-registration/degree/', views.faculty_registration_degree, name='faculty-registration-degree'),
    path('faculty-registration/images/', views.faculty_registration_images, name='faculty-registration-images'),
    path('faculty/<int:pk>', views.UniversityView.as_view(), name='university_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

