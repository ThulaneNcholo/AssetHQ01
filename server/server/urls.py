from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('client.urls')),
    path('accounts/',include('accounts.urls')),
    path('managers/',include('managers.urls')),
    path('owners/',include('owners.urls')),
    path('applications/',include('applications.urls')),
    path('property/',include('property.urls')),
    path('vendors/',include('Vendors.urls')),
    path('tasks/',include('Tasks.urls')),
    path('inspection/',include('Inspection.urls')),
    path('Documents/',include('Documents.urls')),
    path('Requests/',include('Requests.urls')),
    path('Financials/',include('Financials.urls')),
]
