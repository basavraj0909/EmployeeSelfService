from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, ProfileDetailView, ProfileUpdateView, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [

    # Registration and JWT token endpoints
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('', include(router.urls)),
]
