from django.urls import path
from .import views

# images urls 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('financials',views.ListFinancials, name='financials'),
    path('property-financials/<int:id>',views.PropertyFinancials, name='property-financials'), 
    path('add-financial-tenant',views.RentTenantPartial, name='financial-tenant'), 

    # forms start 
    path('expenses/<int:id>',views.ExpensesForm, name='expenses'), 
    path('income/<int:id>',views.IncomeForm, name='income'),
    path('rent/<int:id>',views.RentForm, name='rent'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)