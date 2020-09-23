from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, EmployerViewSet, JobseekerViewSet, VacanciesViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('employers', EmployerViewSet)
router.register('jobseeker', JobseekerViewSet)
router.register('jobs', VacanciesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
