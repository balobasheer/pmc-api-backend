from django.contrib import admin

from .models import Service, NewService

# Register your models here.

admin.site.register(Service)
admin.site.register(NewService)