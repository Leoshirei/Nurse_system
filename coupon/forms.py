from django import forms
from .models import Patient

class PatientsForm(forms.ModelForm):
    name = forms.CharField(max_length = 20)
    surname = forms.CharField(max_length = 20)
    pesel = forms.CharField(max_length = 11)
    class Meta:
        model = Patient
        fields = ['name', 'surname', 'pesel']