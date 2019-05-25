from django.contrib.auth.models import User
from django.db import models

from institutions.models import Institution
from cards.models import Card


class Client(models.Model):
    """
    Model representing a Client.
    """

    # Client personal information
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=15, null=True, blank=False)
    whatsapp_number = models.CharField(max_length=15, null=True, blank=False)
    address_line_1 = models.CharField(max_length=100, null=True, blank=True)
    address_line_2 = models.CharField(max_length=100, null=True, blank=True)
    address_lat_long = models.CharField(max_length=100, null=True, blank=True)
    email_address = models.EmailField(max_length=100)

    surburb = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, default="Zimbabwe")

    gender = models.CharField(max_length=100, null=True)
    national_id = models.CharField(max_length=100, null=True)
    student_id = models.CharField(max_length=100, null=True)
    birthday = models.DateTimeField(auto_now_add=True)

    # Institution information
    institution = models.OneToOneField(Institution, on_delete=models.CASCADE)
    card = models.ManyToManyField(Card)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id
