# form/models.py
from django.db import models

class PotentialUserInformation(models.Model):
    GENDER_CHOICES = [
        ('F', 'Frau'),
        ('M', 'Herr'),
        ('N', 'Keine Angabe'),
    ]

    COUNTRY_CHOICES = [
        ('CH', 'Schweiz'),
        ('DE', 'Deutschland'),
        ('AT', 'Österreich'),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    organization = models.CharField(max_length=100)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES)
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
