from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World!")

def survey_home(request):
    return render(request, 'backend/home.html')

def survey_about(request):
    return render(request, 'backend/about.html')