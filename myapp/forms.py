from django import forms
from django.forms import ModelForm
from myapp.models import Datatabase

class databaseform(forms.ModelForm):
    class Meta:
        model = Datatabase
        fields= ["firstname","lastname", "email", "phone", "desc"]