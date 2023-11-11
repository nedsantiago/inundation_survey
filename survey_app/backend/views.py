from django.shortcuts import render
from django.http import HttpResponse

from backend.user_questions import create_questions_context, create_questions_repeat_labels_context


def hello_world(request):
    return HttpResponse("Hello World!")

def survey_home(request):
    return render(request, 'backend/home.html')

def survey_about(request):
    return render(request, 'backend/about.html')

def survey_form(request):
    # initialize a list of questions
    questions = create_questions_context()
    test_sample = questions[12]
    repeat_labels = create_questions_repeat_labels_context()

    # add the context for the rendering
    context = {
            "questions": questions,
            "test_sample": test_sample,
            "repeat_labels": repeat_labels
        }

    # if request is POST
    if request.method == 'POST':
        for key in context.keys():
            print(f"{key}: {context[key]}")
        # then it must be receiving data from form submission
        # check data validity at server-side
        # add data to the database
        return render(request, 'backend/survey_form.html', context)
    
    # else it was a simple request
    else:
        # render with the context
        return render(request, 'backend/survey_form.html', context)