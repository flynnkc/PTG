"""PTG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import pharmacy_home, BatchListView, ReportsHome, ExpiringMedsReport, OrderListView

#### This list will contain the url patterns at the PHARMACY APP level ####
urlpatterns = [
    path('', pharmacy_home.as_view(), name='pharmacy_home'),
    path('batchlist/', BatchListView.as_view(), name='pharmacy_batches'),
    path('reports/', ReportsHome.as_view(), name='pharmacy_reports'),
    path('reports/ex_med_report/', ExpiringMedsReport.as_view(), name='report_expiring'),
    path('lookup/', OrderListView.as_view(), name='pharmacy_order_lookup'),
]