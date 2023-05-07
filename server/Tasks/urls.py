from django.urls import path
from .import views

# images urls 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('task-list',views.TaskList, name='tasks'),
    path('add-task',views.AddTask, name='add-task'),
    path('add-task/<int:id>',views.AddTask, name='add-task'),
    path('view-task/<int:id>',views.ViewTask, name='view-task'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)