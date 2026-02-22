from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Patient
from .forms import PatientsForm


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_patients')
    else:
        form = AuthenticationForm()
    return render(request, 'coupon/login.html', {'form': form})

@login_required
def show_patient(request):
    patients = Patient.objects.filter(owner = request.user)
    return render(request, 'coupon/list_patient.html', {'patients': patients})

@login_required
def create_patient(request):
    if request.method == 'POST':
        form = PatientsForm(request.POST)
        if form.is_valid():
            patient = form.save(commit = False)
            patient.owner = request.user
            patient.save()
            return redirect('list_patients')
    else:
        form = PatientsForm()
    return render(request, 'coupon/create_patient.html', {'form': form})

@login_required
def delete_patient(request, id):
    patient = get_object_or_404(Patient, id = id, owner = request.user)
    patient.delete()
    return redirect('list_patients')
