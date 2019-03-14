from django.contrib import admin
from . import models

# Register models to add to admin page
# If model in models.py do not have __str__ functions they will display as generic objects
admin.register(models.Drug_Generic)
admin.register(models.Drug_Brand)