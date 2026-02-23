from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Patient, Medical_Task, Task_Status, Habit_Table
from .forms import PatientsForm
import datetime, calendar


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

def detail_patient(request, id):
    patient = get_object_or_404(Patient, id = id, owner = request.user)
    medical_tasks = Medical_Task.objects.all()
    tables = Habit_Table.objects.filter(person = patient)
    return render(request, 'coupon/detail_patient.html', {'patient': patient, 'medical_tasks': medical_tasks, 'tables': tables})

def add_table(request, id):
    patient = get_object_or_404(Patient, id = id, owner = request.user)
    tasks = Medical_Task.objects.all()
    today = datetime.date.today()
    month = today.month
    year = today.year
    days_in_month = calendar.monthrange(today.year, today.month)[1]
    days = []
    for day in range(1, days_in_month + 1):
        days.append(day)
    statuses = Task_Status.objects.all()
    status_dict = {}
    for s in statuses:
        if s.habit_id not in status_dict:
            status_dict[s.habit_id] = {}
        status_dict[s.habit_id][s.date] = s.done
    context = {
        'tasks': tasks,
        'days': days,
        'month': month,
        'year': year,
        'status_dict': status_dict,
        'patient': patient,
    }
    return render(request, 'coupon/add_label.html', context)

def save_table(request, patient_id, month, year):
    print("METHOD:", request.method)
    if request.method == "POST":
        print("POST DATA:", request.POST)
        patient = get_object_or_404(Patient, id=patient_id, owner=request.user)
        table, created = Habit_Table.objects.get_or_create(
            person=patient,
            month=month,
            year=year
        )
        for task in Medical_Task.objects.all():
            today = datetime.date.today()
            days_in_month = calendar.monthrange(year, month)[1]
            for day in range(1, days_in_month + 1):
                date = datetime.date(year, month, day)
                checkbox_name = f"task_{task.id}_{day}"
                is_checked = checkbox_name in request.POST
                Task_Status.objects.update_or_create(
                    table=table,
                    habit=task,
                    date=date,
                    defaults={"done": is_checked}
                )
        return redirect('detail_patient', id = patient_id)
    return redirect('list_patients')

def show_table(request, patient_id, month, year):
    patient = get_object_or_404(Patient, id=patient_id, owner=request.user)
    table = get_object_or_404(
        Habit_Table,
        person=patient,
        month=month,
        year=year
    )
    tasks = Medical_Task.objects.all()
    days_in_month = calendar.monthrange(year, month)[1]
    days = range(1, days_in_month + 1)
    statuses = Task_Status.objects.filter(table=table)
    status_dict = {}
    for s in statuses:
        if s.habit_id not in status_dict:
            status_dict[s.habit_id] = {}
        status_dict[s.habit_id][s.date.day] = s.done
    print("STATUS_DICT:", status_dict)
    return render(request, "coupon/add_label.html", {
        "patient": patient,
        "tasks": tasks,
        "days": days,
        "month": month,
        "year": year,
        "status_dict": status_dict,}
        )
