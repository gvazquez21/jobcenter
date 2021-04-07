from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'candidates/index.html')

@login_required
def profiles(request):

    profile = Profile.objects.filter(user=request.user).order_by('user')
    context = {'profiles': profile}
    return render(request, 'candidates/profile.html', context)

@login_required
def new_profile(request):

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
    context = {'form': form}
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




