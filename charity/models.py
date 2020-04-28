from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64)


class Institution(models.Model):
    FOUNDATION = 'F'
    ORGANIZATION = 'O'
    LOCAL = 'L'
    INSTITUTION_TYPE_CHOICES = [
        (FOUNDATION, 'Fundacja'),
        (ORGANIZATION, 'Organizacja pozarządowa'),
        (LOCAL, 'Zbiórka lokalna'),
    ]
    name = models.CharField(max_length=64)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    institution_type = models.CharField(max_length=20, choices=INSTITUTION_TYPE_CHOICES, default=FOUNDATION)


class Donation(models.Model):
    quantity = models.SmallIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.SmallIntegerField()
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=24)
    pick_up_date = models.DateField()
    pick_up_time = models.DateTimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True, default=None, on_delete=models.CASCADE)
