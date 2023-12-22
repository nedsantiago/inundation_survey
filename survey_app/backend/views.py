from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from backend.user_questions import create_questions_context, create_questions_repeat_labels_context
from django.shortcuts import render
from .forms import NonRepeatingForms, RepeatingForms
from .models import Survey
import logging

from django.forms import formset_factory

# Configure the logging module
logging.basicConfig(filename="survey_website.log",
                    format='%(asctime)s %(message)s',
                    level=logging.DEBUG)

logging.debug("Beginning backend views.py")

def survey_home(request):
    return render(request, 'backend/home.html')

def survey_about(request):
    return render(request, 'backend/about.html')

def survey_form_view(request):

    # initialize a list of questions
    questions = create_questions_context()
    test_sample = questions[12]
    repeat_labels = create_questions_repeat_labels_context()

    # repeat labels
    repeating_labels = ['Ondoy', 'Egay', 'Persistent Rain']

    # create repeating form sets
    repeating_form_sets = formset_factory(NonRepeatingForms, extra=len(repeat_labels))

    # create non repeating form sets
    non_repeating_form_sets = formset_factory(NonRepeatingForms, extra=1)
    
    # if request is POST
    if request.method == 'POST':
        # create a form and add data from request
        form = RepeatingForms(request.POST)
        
        # check validity
        if form.is_valid():
            survey = Survey(
                survey_date = form.cleaned_data["survey_date"],
                survey_address = form.cleaned_data["survey_address"],
                district = form.cleaned_data["district"],
                respondent_age = form.cleaned_data["respondent_age"]
                )
            survey.save()
            return HttpResponseRedirect("/survey")
    else:
        form = RepeatingForms()

    # add the context for the rendering
    context = {
            "questions": questions,
            "test_sample": test_sample,
            "repeat_labels": repeat_labels,
            "form": form
        }

    return render(request, "backend/survey_form.html", context)