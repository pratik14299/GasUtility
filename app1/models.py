# Create your models here.
from django.db import models 
import uuid

# Create your models here.
class Customer(models.Model):
     id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=100)
     account_number = models.CharField(max_length=20, unique=True)

     def __str__(self):
          return f'{self.id} {self.name} {self.account_number}'
     

class ServiceRequest(models.Model):
     Service_Types = (
          ('Gas Leak','Gas Leak'),
          ('New Connection','New Connection'),
          ('Replace','Replace'), 
          #more Services  
          )
     tracking_no = models.UUIDField(primary_key=True,default=uuid.uuid4)
     account = models.ForeignKey(Customer,on_delete=models.CASCADE)
     customer = models.CharField(max_length=100)
     Service_Type = models.CharField(max_length=50,choices=Service_Types)
     request_detials = models.TextField()
     attachment = models.FileField(upload_to='attachments/',blank=True, null=True)
     submitted_at = models.DateTimeField(auto_now_add=True)
     resolved_at = models.DateTimeField(blank=True,null=True)
     status = models.CharField(max_length=50, default='Pending')

     # def __str__(self):
     #      return self.customer
     
class TrackStatus(models.Model):
     tracking_no = models.ForeignKey(ServiceRequest,on_delete=models.CASCADE,related_name='status_updates') 
     resolved_at = models.DateTimeField(blank=True,null=True)
     status = models.CharField(max_length=50, default='Pending')

     def __str__(self):
        return str(self.status)
