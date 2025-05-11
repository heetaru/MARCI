from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.http import JsonResponse
from .filters import FacultyFilter
from django.template.loader import render_to_string
from datetime import date
from .models import Faculty, Degree, Image
from account.models import Students, SavedFaculty
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

def fee_view(faculty_id):
    faculty = Faculty.objects.get(id=faculty_id)
    has_free = False
    has_paid = False
    for degree_cost in faculty.degrees.all():
        if degree_cost.cost == 0:
            has_free = True
        else:
            has_paid = True
    print(f"Passing to context: has_free={has_free}, has_paid={has_paid}")
    context = {
        'faculty': faculty,
        'has_free': has_free,
        'has_paid': has_paid,
    }
    return context

def index(request):
    faculty_list = Faculty.objects.all().distinct()
    user_id = request.session.get('student_id')
    user = Students.objects.get(id=user_id)
    saved_faculty_ids = list(SavedFaculty.objects.filter(student=user).values_list('faculty_id', flat=True))
    filter = FacultyFilter(request.GET, queryset=faculty_list)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_to_string('universities/faculty_template.html', {'filter': filter, 'saved_faculty_ids': saved_faculty_ids})
        return JsonResponse({'html': html})


    if request.method == 'POST':
        faculty_id = request.POST.get('faculty_id')
        save_status = request.POST.get('save_status')
        print(f"faculty_id={faculty_id}, save_status={save_status}")


    return render(request, 'universities/faculty_list.html', {
        'filter': filter,
        'saved_faculty_ids': saved_faculty_ids,
    })

def save_faculty(request):
    data = json.loads(request.body)
    university_id = data.get('university_id')
    is_checked = data.get('is_checked')
    student_id = request.session.get('student_id')
    student = Students.objects.get(id=student_id)
    if is_checked:
        SavedFaculty.objects.create(
            faculty_id=university_id,
            student=student,
        )
    else:
        SavedFaculty.objects.filter(
            faculty_id=university_id,
            student=student
        ).delete()


    return JsonResponse({'status': 'ok', 'received': {'university_id': university_id, 'is_checked': is_checked}})


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
        return redirect("faculty_registration_degree")
    return render(request, 'universities/faculty_registration.html', context)


def faculty_registration_degree(request):
    if request.method == 'POST':
        data = request.POST.dict()
        values = list(data.values())[1:]
        faculty = Faculty.objects.get(id=request.session['faculty_id'])

        for i in range(len(values)//4):
            raw_type = values[0]
            raw_duration = values[1]
            raw_cost = values[2]
            raw_start = values[3]

            # Обробка cost
            cost = float(raw_cost) if raw_cost.strip() != "" else 0.0

            # Обробка semester_start
            try:
                semester_start = date.fromisoformat(raw_start)
            except (ValueError, TypeError):
                semester_start = date.today()

            Degree.objects.create(
                faculty=faculty,
                type=raw_type,
                duration=raw_duration,
                cost=cost,
                semester_start=semester_start
            )
            values = values[4:]

        return redirect("faculty_registration_images")
    return render(request, 'universities/faculty_registration_degree.html', {'faculty_registration_degree': faculty_registration_degree})


def faculty_registration_images(request):
    if request.method == 'POST':
        faculty = Faculty.objects.get(id=request.session['faculty_id'])

        Image.objects.create(faculty=faculty, type='main', image=request.FILES.get('main_image'))
        Image.objects.create(faculty=faculty, type='logo', image=request.FILES.get('logo_image'))

        for image in request.FILES.getlist('additional_image'):
            Image.objects.create(faculty=faculty, type='additional', image=image)

        return redirect("university_view", request.session['faculty_id'])

    return render(request, "universities/faculty_registration_images.html")

class UniversityView(DetailView):
    model = Faculty
    template_name = 'universities/faculty.html'
    context_object_name = 'university'


    #Цей кусок кода, треба шоб на сайт передати окремі змінні, які не можна просто так дістати з бд
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        faculty = self.get_object()
        context['has_free'] = fee_view(faculty.id)["has_free"]
        context['has_paid'] = fee_view(faculty.id)["has_paid"]
        context['main_image'] = faculty.images.filter(type='main').first()
        context['logo_image'] = faculty.images.filter(type='logo').first()
        context['additional_images'] = faculty.images.filter(type='additional')
        return context