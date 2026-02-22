from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            User.append(user)
            return redirect('register/')
    else:
        form = AuthenticationForm()
    return render(request, 'coupon/login.html', {'form': form})
