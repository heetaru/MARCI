
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='list'),
    path('account/', include('account.urls')),
    path('faculty-registration/', views.faculty_registration, name='faculty_registration'),
    path('faculty-registration/degree/', views.faculty_registration_degree, name='faculty_registration_degree'),
    path('faculty-registration/images/', views.faculty_registration_images, name='faculty_registration_images'),
    path('faculty/<int:pk>', views.UniversityView.as_view(), name='university_view'),
    path('ajax/save-faculty/', views.save_faculty, name='save_faculty'),
    path('chat/', views.chat_view, name='chat'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

