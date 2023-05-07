from django.urls import path
from .import views

# images urls 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list-inspections',views.ListInspections, name='list-inspections'),
    path('create-inspections/<int:id>',views.CreateInspection, name='create-inspections'),
    path('share-inspection/<int:id>',views.ShareInspection, name='share-inspection'),
    path('inspection-form/<int:id>',views.InspectionForm, name='inspection-form'),
    path('add-inspection/<int:id>',views.AddInspectionForm, name='add-inspection'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
