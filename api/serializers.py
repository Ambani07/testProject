from rest_framework import serializers
from .models import Employer, Vacancy, Jobseeker
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('id', 'business_reg_cert_no', 'company_name',
                  'contact_name', 'contact_tel', 'contact_address', 'contact_email')


class JobseekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobseeker
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'password')


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'job_duties', 'contract_type',
                  'working_hours', 'basic_salary', 'working_exp', 'req_skills',
                  'sector', 'start_date', 'created_date', 'closing_date')
