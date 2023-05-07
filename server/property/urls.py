from django.urls import path
from .import views

# images urls 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add-property',views.AddProperty, name='add-property'),
    path('properties',views.PropertiesView, name='properties'),
    path('propert-details/<int:id>',views.PropertyDetails, name='propert-details'),
    path('view-property/<int:id>',views.ViewProperty, name='view-property'),
    
    path('content1/<int:id>',views.ContentOne, name='content1'),
    path('content2/<int:id>',views.ContentTwo, name='content2'),

    # New Urls start 
    path('property-applications/<int:id>',views.PropertyApplications, name='applicationsProperty'),
    path('lease/<str:action>/<int:id>/',views.LeaseView, name='lease'),
    path('property-tasks/<int:id>',views.PropertyTasks, name='property-tasks'),
    path('property-inspections/<int:id>',views.PropertyInspections, name='property-inspections'),
    path('property-files/<int:id>',views.PropertyModelFiles, name='property-files'),
    path('property-requests/<int:id>',views.PropertyMaintenanceRequest, name='property-requests'),
    path('financials/<int:id>',views.PropertyFinancialsView, name='financials'),
    path('property-viewings/<int:id>',views.PropertyShowings, name='property-viewings'),
]

htmx_urlpatterns = [
    path('property-applicants',views.PropertyApplicantsView, name='property-applicants'),
]

urlpatterns += htmx_urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)