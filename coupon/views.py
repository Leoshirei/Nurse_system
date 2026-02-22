from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from . import forms
from .models import Pacient


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_pacients')
    else:
        form = AuthenticationForm()
    return render(request, 'coupon/login.html', {'form': form})

@login_required
def show_pacient(request):
    pacients = Pacient.objects.filter(owner = request.user)
    return render(request, 'coupon/list_pacients.html', {'pacients': pacients})
