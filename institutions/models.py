from django.contrib.auth.models import User
from django.db import models

from cards.models import Card


class Institution(models.Model):
    """
    Model representing an Institution.
    """

    # Institution information
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, null=True, blank=False)

    address_line_1 = models.CharField(max_length=100, null=True, blank=True)
    address_line_2 = models.CharField(max_length=100, null=True, blank=True)
    address_lat_long = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=False)
    email_address = models.EmailField(max_length=100)

    surburb = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, default="Zimbabwe")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id
