from django.urls import path, include
from .views import CustomerViewSet, ServiceRequestViewSet, TrackStatusView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'servicerequests', ServiceRequestViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('track/<uuid:tracking_no>/', TrackStatusView.as_view(), name='track-status'),
]
