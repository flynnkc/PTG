from django.contrib import admin
from . import models

# Register models to add to admin page
# If model in models.py do not have __str__ functions they will display as generic objects
admin.site.register(models.Drug_Generic)
admin.site.register(models.Drug_Brand)
admin.site.register(models.Manufacturer_Company)
admin.site.register(models.Location)
admin.site.register(models.Order)
admin.site.register(models.Batch)
admin.site.register(models.Order_Detail)
admin.site.register(models.Batch_Location)
