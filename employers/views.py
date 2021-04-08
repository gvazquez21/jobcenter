from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewVacancyForm
from .models import Vacancy

# Create your views here.

@login_required
def register_vacancy(request):
    user = request.user
    if request.method == "POST":
        form = NewVacancyForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.employer = user
            data.save()
            #return redirect('employers:employer-details')
            return redirect('employers:all-vacancies')

    else:
        form = NewVacancyForm()
    context = {
        #'add_vacancy_page': "active",
        'form': form,
        #'employer': user.id,
        #'rec_navbar': 1,
    }
    return render(request, 'employers/register_vacancy.html', context)

@login_required
def employer_details(request):
    #employer_det = Vacancy.objects.filter(user=request.user).order_by('user')
    context = {
        'rec_home_page': "active",
        'rec_navbar': 1,
        #'employer_details': employer_det,
    }
    return render(request, 'employers/details.html', context)

@login_required
def all_vacancies(request):
    vacancies = Vacancy.objects.filter(employer=request.user).order_by('-date_posted')
    context = {
        'vacancies': vacancies,
    }
    return render(request, 'employers/all_vacancies.html', context)

@login_required
def vacancy_detail(request, slug):
    #user = request.user
    vacancy = get_object_or_404(Vacancy, slug=slug)
    context = {
        'vacancy': vacancy,
    }
    return render(request, 'employers/vacancy_detail.html', context)


@login_required
def edit_vacancy(request, slug):
    #user = request.user
    vacancy = get_object_or_404(Vacancy, slug=slug)

    if request.method == "POST":
        form = NewVacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('employers:vacancy-detail', slug)
    else:
        form = NewVacancyForm(instance=vacancy)
        context = {
        'form': form,
        'vacancy': vacancy,
        }
        return render(request, 'employers/edit_vacancy.html', context)

