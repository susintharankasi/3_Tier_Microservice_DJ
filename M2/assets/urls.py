from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssetViewSet, AuditLogViewSet

# DRF Router for ViewSets
router = DefaultRouter()
router.register(r'assets', AssetViewSet, basename='asset')
router.register(r'audit-logs', AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),  # Include all viewset routes
]
