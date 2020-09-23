from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import Employer, Vacancy, Jobseeker
from .serializers import UserSerializer, \
    EmployerSerializer, VacancySerializer, JobseekerSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class JobseekerViewSet(viewsets.ModelViewSet):
    queryset = Jobseeker.objects.all()
    serializer_class = JobseekerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)


class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)


class VacanciesViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
