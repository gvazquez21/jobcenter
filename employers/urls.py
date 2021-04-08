from django.urls import path
from . import views

app_name = 'employers'

urlpatterns = [
    path('', views.employer_details, name='employer-details'),
    path('register_vacancy/', views.register_vacancy, name='register-vacancy'),
    path('all_vacancies/', views.all_vacancies, name='all-vacancies'),
    path('vacancy_detail/<slug>/', views.vacancy_detail, name='vacancy-detail'),
    path('edit_vacancy/<slug>/', views.edit_vacancy, name='edit-vacancy'),
]