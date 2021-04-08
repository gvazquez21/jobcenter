from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    #Schließt Standard_Authentifizierung_URLS ein.
    path('', include('django.contrib.auth.urls')),

    #Registrierungsseite.
    path('register/', views.register, name='register'),

    #logoutseite


]