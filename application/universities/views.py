from django.shortcuts import render
from django.views.generic import DetailView

from .models import University


def index(request):
    university_list = University.objects.all()
    return render(request, 'universities/university_list.html', {'university_list': university_list})


def registration(request):
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
        University.objects.create(university_name=data['university_name'],
                                  region=data['region'],
                                  fakulty_name=data['fakulty_name'],
                                  rektor_name=data['rektor_name'],
                                  dean_name=data['dean_name'], mail=data['mail'],
                                  date_creation=data['date_creation'],
                                  university_description=data['university_description'],
                                  mg=data.get('mg') == 'on',
                                  bc=data.get('bc') == 'on')
    return render(request, 'universities/university_form.html')

class UniversityView(DetailView):
    model = University
    template_name = 'universities/university.html'
    context_object_name = 'university'