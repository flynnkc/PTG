from django.db import models
from django.contrib.auth.models import User


class Drug_Generic(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    schedule = models.IntegerField(null=True, blank=True)


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True)


class Drug_Brand(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    generic_name = models.ForeignKey(Drug_Generic, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    licence = models.IntegerField()
    pack_size = models.IntegerField(null=True, blank=True)


class Location(models.Model):
    upstream_supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
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


class Receive(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)


class Disburse(models.Model):
    pass