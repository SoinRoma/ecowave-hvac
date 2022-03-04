from django.db import models


# Create your models here.

class FeedbackRequest(models.Model):
    SERVICES = (
        (1, "HVAC installation"),
        (2, "Repairing and maintenance"),
        (3, "Other service"),
    )
    full_name = models.TextField(max_length=255, null=True, blank=True)
    phone = models.TextField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    service = models.IntegerField(null=True, blank=True, choices=SERVICES)
