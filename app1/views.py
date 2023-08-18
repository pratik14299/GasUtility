from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Customer, ServiceRequest, TrackStatus
from .serializer import (
    CustomerSerializer,
    ServiceRequestSerializer,
    TrackStatusSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Get the tracking number of the created service request
        tracking_no = serializer.instance.tracking_no

        headers = self.get_success_headers(serializer.data)
        return Response(
            {"tracking_no": str(tracking_no)},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class TrackStatusView(APIView):
    def get(self, request, tracking_no):
        try:
            service_request = ServiceRequest.objects.get(tracking_no=tracking_no)

            track_statuses = TrackStatus.objects.filter(tracking_no=service_request)

            if track_statuses:
                status_list = [status_obj.status for status_obj in track_statuses]
                resolved_date = (
                    service_request.resolved_at.strftime("%Y-%m-%d %H:%M:%S")
                    if service_request.resolved_at
                    else "Not resolved yet"
                )
                return Response(
                    {
                        "tracking_no": str(tracking_no),
                        "statuses": status_list,
                        "resolved_date": resolved_date,
                    }
                )
            else:
                return Response({"status": "Pending"})
        except ServiceRequest.DoesNotExist:
            return Response(
                {"error": "Tracking number does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
