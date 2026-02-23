from django import forms
from django.contrib.auth.models import User

from .models import Patient

class PatientsForm(forms.ModelForm):
    name = forms.CharField(max_length = 20)
    surname = forms.CharField(max_length = 20)
    pesel = forms.CharField(max_length = 11)
    class Meta:
        model = Patient
        fields = ['name', 'surname', 'pesel']

class NurseForm(forms.Form):
    username = forms.CharField(max_length=20)
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    password = forms.CharField(
        widget=forms.PasswordInput
    )
    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['name'],
            last_name=self.cleaned_data['surname']
        )
        return user