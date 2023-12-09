from django import forms

# class NameForm_test(forms.Form):
#     your_name = forms.CharField(label="Your name", max_length=100)

class NameForm(forms.Form):
    subject = forms.CharField(max_length=100, required=False)
    message = forms.CharField(widget=forms.Textarea, required=False)
    sender = forms.EmailField(required=False)

class SurveyQuestions(forms.Form):
    """This class encapsulates all the questions that make up the non-repeating
    portion of the survey. In this case, this portion focuses on demographic and
    location."""

    # forms to produce
    survey_address = forms.CharField(max_length=100, required=False)

    # cleaning methods
    def clean_survey_address(self):
        data = self.cleaned_data["survey_address"]
        return data

class StormEventsExperienced(forms.Form):
    """This class encapsulates all the questions that make up the repeating
    portion of the survey. In this case, this portion focuses on an individual's
    storm event experience at the location."""
    pass