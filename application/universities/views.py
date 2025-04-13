from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .models import University


def index(request):
    university_list = University.objects.all()
    return render(request, 'universities/fakulty_list.html', {'university_list': university_list})


def fakulty_registration(request):
    context = {}
    if request.method == 'POST':
        data = request.POST.dict()
        mg = data.get('mg') == 'on'
        bc = data.get('bc') == 'on'
        University.objects.create(university_name=data['university_name'],
                                  country=data['country'],
                                  city=data['city'],
                                  fakulty_name=data['fakulty_name'],
                                  mail=data['mail'],
                                  university_description=data['university_description'],
                                  mg=mg,
                                  bc=bc)
        context['mg'] = mg
        context['bc'] = bc
        return redirect("fakulty-registration-degree")
    return render(request, 'universities/fakulty_registration.html', context)

def fakulty_registration_degree(request):
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
    return render(request, 'universities/fakulty_registration_degree.html', {'fakulty_registration_degree': fakulty_registration_degree})




def fakulty_registration_images(request):
    return render(request, "universities/fakulty_registration_images.html")

class UniversityView(DetailView):
    model = University
    template_name = 'universities/fakulty.html'
    context_object_name = 'university'