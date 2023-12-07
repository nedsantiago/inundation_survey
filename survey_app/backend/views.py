from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from backend.user_questions import create_questions_context, create_questions_repeat_labels_context
from django.shortcuts import render
from .forms import NameForm_test
import logging

# Configure the logging module
logging.basicConfig(filename="survey_website.log",
                    format='%(asctime)s %(message)s',
                    level=logging.DEBUG)

logging.debug("Beginning backend views.py")

def survey_home(request):
    return render(request, 'backend/home.html')

def survey_about(request):
    return render(request, 'backend/about.html')

def survey_form(request):
    # initialize a list of questions
    questions = create_questions_context()
    test_sample = questions[12]
    repeat_labels = create_questions_repeat_labels_context()
    
    # if request is POST
    if request.method == 'POST':
        # create a form and add data from request
        form = NameForm_test(request.POST)
        # check validity
        if form.is_valid():
            return HttpResponseRedirect("/")
    else:
        form = NameForm_test()

    # add the context for the rendering
    context = {
            "questions": questions,
            "test_sample": test_sample,
            "repeat_labels": repeat_labels,
            "form": form
        }

    return render(request, "backend/survey_form.html", context)