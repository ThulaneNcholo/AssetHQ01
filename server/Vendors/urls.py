from django.urls import path
from .import views

# images urls 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list-vendors',views.VendorList, name='list-vendors'),
    path('add-vendor',views.AddVendor, name='add-vendor'),
    path('vendor-view/<int:id>',views.VendorView, name='vendor-view'),
    path('vendor-services/<int:id>',views.AddVendorService, name='vendor-services'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)