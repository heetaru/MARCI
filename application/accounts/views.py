from django.shortcuts import render

# Create your views here.

from .models import Students
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.http import JsonResponse
from django.template.loader import render_to_string




def register_view(request):
    if request.method == 'POST':
        data = request.POST.dict()
        users = Students.objects.create(user_name = data['user_name'],
                                     user_mail = data['user_mail'],
                                     user_password = data['user_password']
                                     )
        #request.session['faculty_id'] = faculty.id
        #return redirect("faculty-registration-degree")
    return render(request, 'accounts/registration.html', {})

def login_view(request):
    return render(request, 'accounts/login.html')
