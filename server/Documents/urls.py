from django.urls import path
from .import views

# images urls 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # property files urls 
     path('property-documents',views.PropertyDocuments, name='property-documents'),
     path('property-file-form/<int:id>',views.PropertyFilesForm, name='property-file-form'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
