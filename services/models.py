from django.db import models

from accounts.models import User

# Create your models here.\




 
# Customer name ( data type-alphabet)  auto
# Service type (drop-down, alphabet)
# Nature of Job ( Free text box, text input) 
# Customer phone number ( numeric) auto

# Email auto

# Address (alpha-numeric) 

# Postcode ( Alpha-numeric)auto
# Service type (drop-down, alphabet) required

# Preferred Contact date and time (calendar and time) required
# Photo of the request serices that take in the following format JPEG, PNG, and PDF


class Service(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True, unique=True)
    photo = models.FileField(upload_to='images/')
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class NewService(models.Model):

    REQUEST_STATUS = {
        'accept': 'accept',
        'reject': 'reject',
        'counter': 'counter'
    }

    service_type = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_phone_number = models.CharField(max_length=50, null=True, blank=True)
    customer_email = models.CharField(max_length=100, null=True, blank=True)
    post_code = models.CharField(max_length=200, null=True, blank=True)
    job_nature = models.TextField()
    status = models.CharField(max_length=50, choices=REQUEST_STATUS, default='awaiting...')
    address = models.TextField(null=True, blank=True)
    service_picture = models.FileField(upload_to='Service/images')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Service request for {self.service_type.name}"





