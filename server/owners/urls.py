from django.urls import path
from .import views

# images urls 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('owners',views.OwnersList, name='owners'),
    path('create-owner',views.CreateOwner, name='create-owner'),
    path('create-owner/<int:id>',views.CreateOwner, name='create-owner'),
    path('owners-details/<int:id>',views.OwnerDetails, name='owners-details'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)