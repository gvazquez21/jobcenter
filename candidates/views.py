from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'candidates/index.html')

@login_required
def profiles(request):

    profile = Profile.objects.filter(user=request.user).order_by('user')
    currentuser=request.user
    contains_profile = Profile.objects.filter(user=currentuser).first()
    #print(type(Profile.objects))
    #modelmanager,

    context = {'profiles': profile, 'x': 100, 'contains_profile': contains_profile}
    return render(request, 'candidates/profile.html', context)

@login_required
def new_profile(request):
    #muss prüfe ob ein Profil existiert mit diesem  User:
    # wenn es existiert wieder in der Übersicht mit redirect
    #print("REQUEST", request.user)
    #print("first object :", Profile.objects.filter(user=theuser).first())
    currentuser = request.user

    if request.method != 'POST':
        form = ProfileForm()
    else:
        form = ProfileForm(data=request.POST)
        if form.is_valid():
            #new_profile = form(commit=False)
            #new_profile.user = request.user
            #new_profile.save()
            form.save()
            return redirect('candidates:profiles')

    contains_profile = Profile.objects.filter(user=currentuser).first()
    context = {'form': form, 'contains_profile': contains_profile}


    if contains_profile != None:
        return redirect('candidates:profiles')
    else:
        return render(request, 'candidates/new_profile.html',context)

def edit_profile(request):
    theuser = request.user
    profile = Profile.objects.filter(user=theuser).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = theuser
            data.save()
            return redirect('candidates:profiles')
    else:
        form = ProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'candidates/edit_profile.html', context)




