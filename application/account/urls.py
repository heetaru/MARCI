from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='user_registration'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.account_view, name='account'),
]