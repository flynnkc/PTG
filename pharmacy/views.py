from django.shortcuts import render # Render shortcut, very useful
from django.views import View # Generic View
from django.contrib.auth.mixins import LoginRequiredMixin # Subclass to require login to view
from django.views.generic import ListView # Generic List View
from .models import Batch, Location # Import model for Batch List View and Expiring List View
from .forms import ExpiringMedsForm # Form for Expiring Meds Report


class pharmacy_home(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, "pharmacy/pharmacy_home.html")


class ReportsHome(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, "pharmacy/reports_home.html")


class ExpiringMedsReport(LoginRequiredMixin, ListView):
    template_name = 'pharmacy/form_view.html'

    def get(self, request):

        form = ExpiringMedsForm()

        context = {
            'title': 'Expiring Medicine Report',
            'header': 'Medication Expiring Within 120 Days',
            'form': form,
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = ExpiringMedsForm()

        if request.method == 'POST':
            form = ExpiringMedsForm(request.POST)
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


class BatchListView(LoginRequiredMixin, ListView):
    model = Batch

    template_name = 'pharmacy/list_view.html'