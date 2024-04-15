from django.db import models
from django.core.validators import FileExtensionValidator

from accounts.models import User

# Create your models here.\


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
        'pending': 'pending',
        'in progress': 'in progress',
        'done': 'done'
    }

    service_type = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    customer_phone_number = models.CharField(max_length=50, null=True, blank=True)
    customer_email = models.CharField(max_length=100, null=True, blank=True)
    post_code = models.CharField(max_length=200, null=True, blank=True)
    job_nature = models.TextField()
    status = models.CharField(max_length=50, choices=REQUEST_STATUS, default='awaiting...')
    address = models.TextField(null=True, blank=True)
    service_picture = models.FileField(upload_to='Service/images', 
                        validators=[FileExtensionValidator(['pdf','jpeg', 'jpg', 'png'])])
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Service request for {self.service_type.name}"

