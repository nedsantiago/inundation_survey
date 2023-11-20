from django import forms

class NameForm_test(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)