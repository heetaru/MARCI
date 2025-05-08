from django.shortcuts import render

# Create your views here.

from .models import Users
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.http import JsonResponse
from django.template.loader import render_to_string




def register_view(request):
    if request.method == 'POST':
        data = request.POST.dict()
        users = Users.objects.create(user_name = data['user_name'],
                                     user_mail = data['user_mail'],
                                     user_password = data['user_password']
                                     )

        #request.session['faculty_id'] = faculty.id
        return redirect("faculty-registration-degree")
    return render(request, 'universities/faculty_registration.html', context)
    return render(request, 'accounts/registration.html')

def login_view(request):
    return render(request, 'accounts/login.html')

def faculty_registration(request):
    context = {}
    if request.method == 'POST':
        data = request.POST.dict()
        faculty = Faculty.objects.create(university_name=data['university_name'],
                                         country=data['country'],
                                         city=data['city'],
                                         faculty_name=data['faculty_name'],
                                         mail=data['mail'],
                                         university_description=data['university_description'],
                                         )
        request.session['faculty_id'] = faculty.id
        return redirect("faculty-registration-degree")
    return render(request, 'universities/faculty_registration.html', context)