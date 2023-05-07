from django.shortcuts import render,redirect
from django.contrib import messages 
import random
from .models import *

# other models 
from property.models import PropertyModel
from managers.models import ManagerModel
from owners.models import OwnerModel
from applications.models import ApplicationModel

# Create your views here.
def PropertyDocuments(request):
    properties_files = PropertyDocument.objects.all().order_by('-date_created')

    # forms data 
    properties = PropertyModel.objects.all()

    context = {
        "properties_files" : properties_files,
        "properties" : properties
    }

    return render(request,'Documents/property_documents.html',context)

# Property Files Form 
def PropertyFilesForm(request,id):
    property = PropertyModel.objects.get(id = id)

    # save Property File 
    if request.method == 'POST' and 'submit_file' in request.POST:
        save_property_file = PropertyDocument()
        save_property_file.property = property
        save_property_file.name = request.POST.get('name')
        save_property_file.description = request.POST.get('file_description')
        save_property_file.file = request.FILES['file']
        save_property_file.save()
        messages.success(request,'New File Added') 
        return redirect('property-documents')

    context = {
        "property" : property
    }
    return render(request,'forms/property_files_form.html',context)
    
