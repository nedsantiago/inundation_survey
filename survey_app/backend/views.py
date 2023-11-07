from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World!")

def survey_home(request):
    return render(request, 'backend/home.html')

def survey_about(request):
    return render(request, 'backend/about.html')

def survey_form(request):
    # if request is POST
    if request.method == 'POST':
        context = {
            "survey_date": request.POST.get('survey_date'),
            "survey_address": request.POST.get('survey_address'),
            "respondent_name": request.POST.get('respondent_name'),
            "respondent_age": request.POST.get('respondent_age'),
            "respondent_residency_type_resident": request.POST.get('respondent_residency_type_resident'),
            "respondent_residency_type_employee": request.POST.get('respondent_residency_type_employee')
        }
        for key in context.keys():
            print(f"{key}: {context[key]}")
        # then it must be receiving data from form submission
        # check data validity at server-side
        # add data to the database
        return render(request, 'backend/survey_form.html')
    else:
        return render(request, 'backend/survey_form.html')