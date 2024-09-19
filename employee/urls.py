from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, ProfileDetailView, ProfileUpdateView

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('', include(router.urls)),
]
