from django import forms

import datetime
from .models import Survey, StormExperienced

class NameForm(forms.Form):
    subject = forms.CharField(max_length=100, required=False)
    message = forms.CharField(widget=forms.Textarea, required=False)
    sender = forms.EmailField(required=False)

class NonRepeatingForms(forms.ModelForm):
    """This class encapsulates all the questions that make up the non-repeating
    portion of the survey. In this case, this portion focuses on demographic and
    location."""

    class Meta:
        model = Survey
        fields = '__all__'

class RepeatingForms(forms.ModelForm):
    """This class encapsulates all the questions that make up the repeating
    portion of the survey. In this case, this portion focuses on an individual's
    storm event experience at the location."""

    class Meta:
        model = StormExperienced
        fields = [
            "storm_name",
            "survey_encode_datetime",
            "encoder_email_ad",
            "storm_duration",
            "storm_originate",
            "storm_warning",
            "storm_did_evacuate",
            "storm_evacuate_loc",
            "storm_evacuate_floodtime",
            "storm_transpo",
            "storm_disease",
            "storm_loss",
            "storm_work_school",
            "storm_days_no_ws",
            "storm_walkability",
            "image"
            ]
        # widgets = {
        #     "storm_name":
        # }