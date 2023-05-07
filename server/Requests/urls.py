from django.urls import path
from .import views

# images urls 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list-requests',views.ListRequests, name='list-requests'),  
    path('maintenance-request/<int:id>',views.RequestForm, name='maintenance-request'),
    path('request-details/<int:id>',views.RequestDetails, name='request-details'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)