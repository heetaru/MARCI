from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .filters import FacultyFilter

from .models import Faculty, Degree, Image

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
    filter = FacultyFilter(request.GET, queryset=faculty_list)
    return render(request, 'universities/faculty_list.html', {
        'filter': filter
    })


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


def faculty_registration_degree(request):
    if request.method == 'POST':
        data = request.POST.dict()
        values = list(data.values())[1:]
        faculty = Faculty.objects.get(id=request.session['faculty_id'])

        for i in range(len(values)//3):
            Degree.objects.create(
                faculty=faculty,
                type=values[0],
                duration=values[1],
                cost=values[2]
            )
            values = values[3:]

        return redirect("faculty-registration-images")
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