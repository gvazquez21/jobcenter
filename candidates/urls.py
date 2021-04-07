"""Defines  URL patterns for candidates"""
from django.urls import path

from . import views

app_name = 'candidates'
urlpatterns= [
    #Startseite
    path('', views.index, name='index'),

    # Seite die die Candidates anzeigt
    path('profiles/', views.profiles, name='profiles'),


    #Neuer Kandidat
    path('new_profile/', views.new_profile, name='new_profile'),

    #Seite zum Bearbeiten einer Profile
    path('edit_profile/', views.edit_profile,name='edit_profile')


]