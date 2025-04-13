from django.shortcuts import render
from django.views.generic import DetailView

from .models import University


def index(request):
    university_list = University.objects.all()
    return render(request, 'universities/university_list.html', {'university_list': university_list})


def registration(request):
    context = {}
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
        mg = data.get('mg') == 'on'
        bc = data.get('bc') == 'on'
        University.objects.create(university_name=data['university_name'],
                                  country=data['country'],
                                  city=data['city'],
                                  fakulty_name=data['fakulty_name'],
                                  mail=data['mail'],
                                  date_creation=data['date_creation'],
                                  university_description=data['university_description'],
                                  mg=mg,
                                  bc=bc)
        context['mg'] = mg
        context['bc'] = bc
    return render(request, 'universities/university_form.html', context)

class UniversityView(DetailView):
    model = University
    template_name = 'universities/university.html'
    context_object_name = 'university'