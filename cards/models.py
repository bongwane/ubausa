from django.db import models

class Card(models.Model):
    """
    Model representing a Client.
    """
    # Card data

    card_number = models.CharField(max_length=100, null=True, blank=False)
    card_limit = models.CharField(max_length=100, null=True, blank=False)
    card_status = models.CharField(max_length=100, null=True, blank=False)

    provider = models.CharField(max_length=100, null=True, blank=True)
    expiry_date = updated_at = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id
