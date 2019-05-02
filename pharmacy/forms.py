from django.forms import Form, ModelForm, ModelChoiceField, CharField
from pharmacy.models import Location, Order
"""
class SearchForm(ModelForm):

    class Meta:
        model = Search
        fields = ['barcode', 'generic_name', 'manufacturer_company', 'name', 'license', 'dose', 'does_count']

        form = SearchForm()

        search = Search.objects.get(pk=1)
        form = SearchForm(instance = Search)
"""

class ExpiringMedsForm(Form):
    query = Location.objects.all()
    name = ModelChoiceField(query, empty_label='All',label='Location Name',required=False)


class OrderLookupForm(ModelForm):
    class Meta:
        model = Order
        fields = ['location_from', 'location_to', 'user', 'date_time', 'state'] # OR __all__

class AddInventoryForm(Form):
    barcode = CharField()

class AddInventoryForm2(Form):
    query = Location.objects.all()
    location = ModelChoiceField(query, empty_label='Please Select Your Location', label='Location Name', required = True)
"""
class AddInventoryForm3(Form):
    query = 
"""