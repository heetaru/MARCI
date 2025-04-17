from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .models import Faculty, Degree, Image


def index(request):
    university_list = Faculty.objects.all()
    return render(request, 'universities/fakulty_list.html', {'university_list': university_list})


def fakulty_registration(request):
    context = {}
    if request.method == 'POST':
        data = request.POST.dict()
        faculty = Faculty.objects.create(university_name=data['university_name'],
                                         country=data['country'],
                                         city=data['city'],
                                         fakulty_name=data['fakulty_name'],
                                         mail=data['mail'],
                                         university_description=data['university_description'],
                                         )
        request.session['faculty_id'] = faculty.id
        return redirect("fakulty-registration-degree")
    return render(request, 'universities/fakulty_registration.html', context)


def fakulty_registration_degree(request):
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

        return redirect("fakulty-registration-images")
    return render(request, 'universities/fakulty_registration_degree.html', {'fakulty_registration_degree': fakulty_registration_degree})


def fakulty_registration_images(request):
    if request.method == 'POST':
        faculty = Faculty.objects.get(id=request.session['faculty_id'])

        Image.objects.create(faculty=faculty, type='main', image=request.FILES.get('main_image'))
        Image.objects.create(faculty=faculty, type='logo', image=request.FILES.get('logo_image'))

        for image in request.FILES.getlist('additional_image'):
            Image.objects.create(faculty=faculty, type='additional', image=image)

    return render(request, "universities/fakulty_registration_images.html")

class UniversityView(DetailView):
    model = Faculty
    template_name = 'universities/fakulty.html'
    context_object_name = 'university'

    #Цей кусок кода, треба шоб на сайт передати окремі змінні, які не можна просто так дістати з бд
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        faculty = self.get_object()
        context['main_image'] = faculty.images.filter(type='main').first()
        context['logo_image'] = faculty.images.filter(type='logo').first()
        context['additional_images'] = faculty.images.filter(type='additional')
        return context