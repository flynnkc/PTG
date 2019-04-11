from django.forms import Form, ModelChoiceField
from pharmacy.models import Drug_Brand, Location
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
    name = ModelChoiceField(query, empty_label=None)

class AddInventoryForm(Form):
    query = Location.objects.all()
    name = ModelChoiceField(query, empty_label=None)
