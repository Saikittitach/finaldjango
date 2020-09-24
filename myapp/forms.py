from django import forms

class NameForm(forms.Form):
    your_firstname = forms.CharField(label='firstname', max_length=128)
