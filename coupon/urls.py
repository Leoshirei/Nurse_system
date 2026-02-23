from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_patient, name = 'list_patients'),
    path('create/', views.create_patient, name = 'create_patient'),
    path('<int:id>/delete/', views.delete_patient, name = 'delete_patient'),
    path('<int:id>/detail/', views.detail_patient, name = 'detail_patient'),
    path('add_table/<int:id>/', views.add_table, name = 'add_table'),
    path('tracker/<int:patient_id>/<int:month>/<int:year>/save/', views.save_table, name = 'save_table'),
    path('tracker/<int:patient_id>/<int:month>/<int:year>/', views.show_table, name = 'show_table'),
]