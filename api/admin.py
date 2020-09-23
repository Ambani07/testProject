from django.contrib import admin
from .models import Employer, Vacancy, Jobseeker

admin.site.register(Employer)
admin.site.register(Jobseeker)
admin.site.register(Vacancy)

