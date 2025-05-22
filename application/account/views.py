from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import Students
from universities.models import Faculty
from account.models import Students, SavedFaculty


def register_view(request):
    if request.method == 'POST':
        data = request.POST
        Students.objects.create(
            user_name=data['user_name'],
            user_mail=data['user_mail'],
            user_password=make_password(data['user_password'])
        )
        return redirect('login')
    return render(request, 'account/registration.html')


def login_view(request):
    if request.method == 'POST':
        data = request.POST
        user_mail_login = data['user_mail_login']
        user_password_login = data['user_password_login']
        student = Students.objects.filter(user_mail=user_mail_login).first()
        if student and check_password(user_password_login, student.user_password):
            request.session['student_id'] = student.id
            request.session['student_name'] = student.user_name
            return redirect('account')

    return render(request, 'account/login.html' )


def account_view(request):
    faculties = Faculty.objects.all()
    user_id = request.session.get('student_id')
    student = Students.objects.get(id=user_id)
    saved_faculty_ids = list(SavedFaculty.objects.filter(student=student).values_list('faculty_id', flat=True))
    liked_faculties = []
    for like_id in saved_faculty_ids:
        if like_id not in liked_faculties:
            liked_faculties.append(Faculty.objects.get(id=like_id))


    if 'student_id' not in request.session:
        return redirect('login')
    return render(request, 'account/account.html', {
        'faculties': faculties,
        'saved_faculty_ids': saved_faculty_ids,
        'student': student,
        'liked_faculties': liked_faculties,
    })


def logout_view(request):
    request.session.flush()
    return redirect('login')
