from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_patient, name = 'list_patients'),
    path('create/', views.create_patient, name = 'create_patient'),
]