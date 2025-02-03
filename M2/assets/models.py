from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Asset(models.Model):
    ASSET_TYPES = [
        ('Hardware', 'Hardware'),
        ('Software', 'Software'),
        ('License', 'License'),
    ]
    
    name = models.CharField(max_length=255)
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPES)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    purchase_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)  # For licenses
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Decommissioned', 'Decommissioned')], default='Active')

    def is_expired(self):
        return self.expiry_date and self.expiry_date < now().date()

    def __str__(self):
        return f"{self.name} ({self.asset_type})"

class AuditLog(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} - {self.asset.name} by {self.user.username}"
