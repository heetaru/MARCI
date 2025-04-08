from django.shortcuts import render

def index(request):
    return render(request, 'universities/university_list.html')


def registration(request):
    return render(request, 'universities/university_form.html')