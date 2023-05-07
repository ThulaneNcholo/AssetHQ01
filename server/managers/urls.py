from django.urls import path
from .import views

# images urls 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add-manager',views.AddManager, name='add-manager'),
    path('add-manager/<int:id>',views.AddManager, name='add-manager'),
    path('managers',views.ManagersList, name='managers'),
    path('manager-details/<int:id>',views.ManagerDetails, name='manager-details'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
