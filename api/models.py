from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Employer(models.Model):
    business_reg_cert_no = models.CharField(max_length=255, blank=False)
    company_name = models.CharField(max_length=255, blank=False)
    contact_name = models.CharField(max_length=255, blank=False)
    contact_tel = models.CharField(max_length=255, blank=True)
    contact_address = models.CharField(max_length=255, blank=False)
    contact_email = models.CharField(max_length=255, blank=True)

    def vacancies(self):
        return Vacancy.objects.filter(employer=self)


class Jobseeker(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=10, blank=False)
    password = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=255, blank=False)


class Vacancy(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    job_duties = models.CharField(max_length=255, blank=False)
    contract_type = models.CharField(max_length=100, blank=True)
    working_hours = models.IntegerField(blank=True)
    basic_salary = models.DecimalField(max_digits=11, decimal_places=2, blank=True)
    working_exp = models.CharField(max_length=255, blank=True)
    req_skills = models.CharField(max_length=255, blank=False)
    sector = models.CharField(max_length=255)
    start_date = models.DateField(null=True)
    created_date = models.DateTimeField(default=now, editable=False)
    closing_date = models.DateTimeField(blank=False)
