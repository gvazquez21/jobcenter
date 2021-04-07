from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """ Register a new user. """
    if request.method != 'POST':
        form = UserCreationForm(request.POST)
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            #new_user = form.save()
            #login(request, new_user)ikikü
            return redirect('candidates:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)


