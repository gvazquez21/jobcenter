from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField   #pip install django-autoslug

# Create your models here.
CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)

class Vacancy(models.Model):
    employer = models.ForeignKey(
        User, related_name='vacancies', on_delete=models.CASCADE)
    # related_name recherchieren
    vacancy_title = models.CharField(max_length=228)
    organisation = models.CharField(max_length=221)
    location_vacancy = models.CharField(max_length=221)
    basic_info_vacancy = models.TextField()
    type_employment = models.CharField(
        max_length=33, choices=CHOICES, default='Full Time', null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    slug = AutoSlugField(populate_from='vacancy_title', unique=True, null=True)

    def __str__(self):
        return self.vacancy_title