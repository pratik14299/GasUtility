from django.contrib import admin
# Register your models here.
from .models import Customer, ServiceRequest,TrackStatus


class CustAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ['id','name','account_number' ]

class ServiceRequestAdmin(admin.ModelAdmin):
    model = ServiceRequest
    list_display = ['account','customer','Service_Type','submitted_at' ]

class TrackStatusAdmin(admin.ModelAdmin):
    model = TrackStatus 
    list_display = [ 'tracking_no','resolved_at','status']
   

admin.site.register(Customer, CustAdmin)
admin.site.register(ServiceRequest,ServiceRequestAdmin)
admin.site.register(TrackStatus,TrackStatusAdmin) 