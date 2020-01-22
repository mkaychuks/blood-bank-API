from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField


BLOOD_GROUP = [
    ('A Positive', 'A+'),
    ('A Negative', 'A-'),
    ('AB Positive', 'AB+'),
    ('AB Negative', 'AB-'),
    ('B Positive', 'B+'),
    ('B Negative', 'B-'),
    ('O Positive', 'O+'),
    ('O Negative', 'O-'),
]


class Donor(models.Model):
    full_name = models.CharField(max_length=100)
    mobile_number = PhoneNumberField(max_length=21, unique=True)
    address = models.TextField()
    age = models.PositiveIntegerField()
    blood_group = models.CharField(choices=BLOOD_GROUP, max_length=21)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='details')

    def __str__(self):
        return self.full_name
