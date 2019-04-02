from django.forms import ModelForm
from pharmacy.models import Drug_Brand
"""
class SearchForm(ModelForm):

    class Meta:
        model = Search
        fields = ['barcode', 'generic_name', 'manufacturer_company', 'name', 'license', 'dose', 'does_count']

        form = SearchForm()

        search = Search.objects.get(pk=1)
        form = SearchForm(instance = Search)
"""