from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.shortcuts import render
from .forms import NonRepeatingForms
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

def survey_form_view(request):

    # create non repeating form sets
    non_repeating_entries = NonRepeatingForms()
    
    # if request is POST
    if request.method == 'POST':
        # create a form and add data from request
        form = NonRepeatingForms(request.POST)

        # check what is in request POST
        logging.debug(f"POST has: {request.POST}")
        
        # check validity
        is_valid = form.is_valid()
        logging.debug(f"validity of the received data is: {is_valid}")
        if form.is_valid():
            logging.debug("Beginning form recording")
            form.save()
            logging.debug("Form was saved")
        return HttpResponseRedirect("/survey")
    else:
        form = non_repeating_entries

    # add the context for the rendering
    context = {
            "form": form
        }

    return render(request, "backend/survey_form.html", context)