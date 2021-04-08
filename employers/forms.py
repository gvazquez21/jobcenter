from django import forms
from .models import Vacancy


class NewVacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        #fields = ['employer','vacancy_title', 'organisation', 'location_vacancy', 'basic_info_vacancy','type_employment']
        fields = ['vacancy_title', 'organisation', 'location_vacancy', 'basic_info_vacancy','type_employment']
    """
        widgets = {
            'employer': forms.HiddenInput(),
        }
    """