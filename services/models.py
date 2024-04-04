from django.db import models

from accounts.models import User

# Create your models here.\




 
# Customer name ( data type-alphabet)  auto
# Service type (drop-down, alphabet)
# Nature of Job ( Free text box, text input) 
# Customer phone number ( numeric) auto

# Email auto

# Address (alpha-numeric) uto

# Postcode ( Alpha-numeric)auto
# Service type (drop-down, alphabet) required

# Preferred Contact date and time (calendar and time) required
# Photo of the request serices that take in the following format JPEG, PNG, and PDF


class Service(models.Model):
    
