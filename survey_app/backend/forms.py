from django import forms

# class NameForm_test(forms.Form):
#     your_name = forms.CharField(label="Your name", max_length=100)

class NameForm_test(forms.Form):
    subject = forms.CharField(max_length=100, required=False)
    message = forms.CharField(widget=forms.Textarea, required=False)
    sender = forms.EmailField(required=False)
    cc_myself = forms.BooleanField(required=False)