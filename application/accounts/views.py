from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.http import JsonResponse
from django.template.loader import render_to_string




def register_view(request):
    return render(request, 'accounts/registration.html')

def login_view(request):
    return render(request, 'accounts/login.html')
