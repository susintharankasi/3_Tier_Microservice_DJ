# Register your models here.
from django.contrib import admin
from .models import Asset, AuditLog

admin.site.register(Asset)
admin.site.register(AuditLog)
