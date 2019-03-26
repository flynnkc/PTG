from django.db import models
from django.contrib.auth.models import User

class Drug_Generic(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    schedule = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Manufacturer_Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return self.name

class Drug_Brand(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    generic_name = models.ForeignKey(Drug_Generic, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer_Company, on_delete=models.CASCADE)
    license = models.IntegerField()
    dose = models.TextField(null=True, blank=True)
    pack_size = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=80)
    upstream_supplier = models.IntegerField(null=True, blank=True)
    is_hospital = models.BooleanField(default=False)
    is_clinic = models.BooleanField(default=False)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name

class Order(models.Model):
    location_from = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Location_Origin')
    location_to = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Location_Destination')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #MODIFY DATE FIELD TO FORMAT DESIRED BY RAPULA
    date_time = models.DateField()
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.state

#ORDER_DETAIL ASSOCIATIVE ENTITY ATTEMPT
# https://stackoverflow.com/questions/28712848/composite-primary-key-in-django/28712960#28712960
class Order_Detail(models.Model):
    class Meta:
        unique_together = (('order_id','barcode'),)
    order_id = models.IntegerField(primary_key=True)
    barcode = models.IntegerField()
    count = models.IntegerField(null=True, blank=True)

class Batch(models.Model):
    drug_brand = models.ForeignKey(Drug_Brand, on_delete=models.CASCADE)
    #MODIFY DATE FIELD TO FORMAT DESIRED BY RAPULA
    expiration_date = models.DateField()
    #Batch size is allowed to be null, change if it needs to have the batch size.
    batch_size = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.drug_brand

#Batch_Location ASSOCIATIVE ENTITY ATTEMPT
# https://stackoverflow.com/questions/28712848/composite-primary-key-in-django/28712960#28712960
class Batch_Location(models.Model):
    class Meta:
        unique_together = (('batch_id','location_id'),)
    batch_id = models.IntegerField(primary_key=True)
    location_id = models.IntegerField()
    count = models.IntegerField(null=True, blank=True)