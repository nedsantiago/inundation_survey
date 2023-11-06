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
        survey_date = request.POST.get('survey_date')
        print(f"survey_date: {survey_date}")
        # then it must be receiving data from form submission
        # check data validity at server-side
        # add data to the database
        return render(request, 'backend/survey_form.html')
    else:
        return render(request, 'backend/survey_form.html')