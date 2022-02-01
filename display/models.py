import datetime

from django.db import models
from django.contrib.auth.models import User

"""
Choices field for gender, country and city
"""
GENDER_CHOICES = (
    ('male','MALE'),
    ('female', 'FEMALE'),
    ('others','OTHERS'),
)

COUNTRY_CHOICES = (
    ('russia','RUSSIA'),
    ('indonesia', 'INDONESIA'),
    ('ukraine','UKRAINE'),
)

CITY_CHOICES = (
    ('leviv','LEVIV'),
    ('sasovo', 'SASOVO'),
    ('klatakan','KLATAKAN'),
)

# Create your models here.
class Profile(models.Model):
    """
    Model to store the list of all profiles
    """
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    email = models.EmailField(
        max_length=50,
        unique=True,
        blank=True,
        null=True
    )

    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default='male'
    )

    country = models.CharField(
        max_length=10,
        choices=COUNTRY_CHOICES,
        default='russia'
    )

    city = models.CharField(
        max_length=10,
        choices=CITY_CHOICES,
        default='leviv'
    )

    date_of_birth = models.DateField(
        default=datetime.date.today
    )

    def __str__(self):
        """
        Returns the name and email address of the person
        """
        return f"{self.name} {self.email}"




    


