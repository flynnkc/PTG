from django.forms import Form, ModelForm, ModelChoiceField
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
    query = Location.objects.all() # Query to grab all instances of Location
    name = ModelChoiceField(query, empty_label='All', label='Location Name', required=False)


class OrderLookupForm(ModelForm):
    class Meta:
        model = Order
        fields = ['location_from', 'location_to', 'user', 'date_time', 'state'] # OR __all__