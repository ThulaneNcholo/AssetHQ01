from django.urls import path
from .import views

# images urls 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create-application',views.CreateApplication, name='create-application'),
    path('create-application/<int:id>',views.CreateApplication, name='create-application'),
    path('application-details/<int:id>',views.ApplicationDetails, name='application-details'),

    # Rentals urls 
    path('rentals',views.RentalApplications, name='rentals'),

    # Buyers urls 
    path('buyers',views.BuyerApplications, name='buyers'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
