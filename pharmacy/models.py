from django.db import models
from django.contrib.auth.models import User

# This file is for models
# Reference https://docs.djangoproject.com/en/2.1/topics/db/models/
class Drug_Generic(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    schedule = models.IntegerField(null=True, blank=True)


class Manufacturer_Company(models.Model):
    manufacturer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True)


class Drug_Brand(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    generic_name = models.ForeignKey(Drug_Generic, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer_Company, on_delete=models.CASCADE)
    licence = models.IntegerField()


class Location(models.Model):
    name = models.CharField(max_length=80)
    is_hospital = models.BooleanField(default=False)
    is_clinic = models.BooleanField(default=False)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=14)


# Use barcode for the primary key on Drug model
class Drug(models.Model):
    barcode = models.IntegerField(primary_key=True)
    name = models.ForeignKey(Drug_Brand, on_delete=models.CASCADE)
    location = models.ManyToManyField(Location)
    batch_lot = models.IntegerField()
    dose = models.CharField(max_length=20, blank=True)
    count = models.IntegerField()
    expiration_date = models.DateField()
    checked_out = models.BooleanField(null=True, blank=True)
    reason = models.TextField(null=True, blank=True)


class Receive(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)


class Disburse(models.Model):
    pass