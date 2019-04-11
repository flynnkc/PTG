from datetime import date, timedelta # For Expiring Meds Report time calculations
from django.shortcuts import render # Render shortcut, very useful
from django.views import View # Generic View
from django.contrib.auth.mixins import LoginRequiredMixin # Subclass to require login to view
from django.views.generic import ListView # Generic List View
from .models import Batch, Location, Batch_Location # Import model for Batch List View and Expiring List View
from .forms import ExpiringMedsForm # Form for Expiring Meds Report
from .forms import AddInventoryForm

class pharmacy_home(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, "pharmacy/pharmacy_home.html")


class ReportsHome(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, "pharmacy/reports_home.html")


class ExpiringMedsReport(LoginRequiredMixin, View):
    template_name = 'pharmacy/form_view.html'

    # This method will be processed when ExpiringMedsReport view is accessed via get method
    def get(self, request):

        form = ExpiringMedsForm()

        context = {
            'title': 'Expiring Medicine Report',
            'header': 'Medication Expiring Within 120 Days',
            'form': form,
        }
        return render(request, self.template_name, context=context)

    # This method will be processed when ExpiringMedsReport view is accessed via post method
    def post(self, request):
        form = ExpiringMedsForm()

        # Double check on request method used
        if request.method == 'POST':
            # Binds data to form for validation
            form = ExpiringMedsForm(request.POST)

            if form.is_valid():

                # If form name attribute comes back empty, assume user wants data for all locations
                if(form.cleaned_data['name'] is None):
                    batch_query = Batch_Location.objects.filter(batch_id_id__expiration_date__lte=(date.today()+timedelta(days=120)))
                    batch_query = batch_query.filter(count__gt=0)
                    batch_query = batch_query.order_by('batch_id_id__expiration_date')

                else:
                    # Get Location Primary Key and assign to place, then perform Django ORM query for medicines expiring in the next 120 days
                    place = Location.objects.filter(name__exact=form.cleaned_data['name']) # FROM Location WHERE name = ['name']
                    place = place.values('id') # SELECT id

                    '''     This does the same as the below statment. QuerySet objects can be chained or modified in multiple statments.
                            No call to database occurs until batch_query is passed to page context.
                    batch_query = Batch_Location.objects.filter(location_id_id=place[0]['id']).filter(
                        batch_id_id__expiration_date__lte=(date.today() + timedelta(days=120))
                        ).order_by('batch_id_id__expiration_date') '''

                    # SELECT * FROM Batch_Location
                    batch_query = Batch_Location.objects.filter(location_id_id=place[0]['id']) # WHERE Location_ID = place['id']
                    batch_query = batch_query.filter(batch_id_id__expiration_date__lte=(date.today()+timedelta(days=120))) # AND Expiration_Date <= 120 days
                    batch_query = batch_query.filter(count__gt=0) # AND count > 0
                    batch_query = batch_query.order_by('batch_id_id__expiration_date') # ORDER BY Batch.Expiration_Date

                # Pass the results of the query back in the page context to be iterated over and displayed by the template
                context = {
                    'title': 'Expiring Medicine Report',
                    'header': 'Medicine Expiring Within 120 days - %s' % form.cleaned_data['name'],
                    'form': form,
                    'inventories': batch_query,
                }

                return render(request, self.template_name, context=context)

            # If something goes wrong with the form, a blank form will be served
            else:
                context = {
                    'title': 'Expiring Medicine Report',
                    'header': 'Something went wrong. Sorry!',
                    'form': form,
                }
                return render(request, self.template_name, context=context)


class BatchListView(LoginRequiredMixin, ListView):
    model = Batch

    template_name = 'pharmacy/list_view.html'

class AddInventory(LoginRequiredMixin, ListView):
    template_name = 'pharmacy/form_view.html'

    def get(self, request):

        form = AddInventoryForm()

        context = {
            'title': 'Expiring Medicine Report',
            'header': 'Medication Expiring Within 120 Days',
            'form': form,
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = AddInventoryForm()

        if request.method == 'POST':
            form = AddInventoryForm(request.POST)
            if form.is_valid():

                
                context = {
                    'title': 'Test',
                    'header': 'Thanks!',
                    'form': form,
                }

                return render(request, self.template_name, context=context)

            else:
                context = {
                    'title': 'Expiring Medicine Report',
                    'header': 'Something went wrong. Sorry!',
                    'form': form,
                }
                return render(request, self.template_name, context=context)
