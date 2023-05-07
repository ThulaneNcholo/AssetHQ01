from django.shortcuts import render,redirect
from django.contrib import messages 
import random
from .models import *

# other models 
from property.models import PropertyModel
from managers.models import ManagerModel
from owners.models import OwnerModel
from applications.models import ApplicationModel
from Vendors.models import VendorModel

# Create your views here.

# list all request 
def ListRequests(request):
    properties = PropertyModel.objects.all()
    maintenance_requests = MaintenanceRequest.objects.all().order_by('-date_created')

    context = {
        "properties" : properties,
        "maintenance_requests" : maintenance_requests
    }
    
    return render(request,'Requests/list_request.html',context)

# Maintenance Form 
def RequestForm(request,id):
    property = PropertyModel.objects.get(id = id)
    priorityStatus = PriorityModel.objects.all()
    maintenance_status = MaintenanceStatusModel.objects.get(name = 'Pending')

    # Save Maintenance Request 
    if request.method == 'POST' and 'submit_request' in request.POST:
        save_request = MaintenanceRequest()
        save_request.property = property
        save_request.title = request.POST.get('title')
        save_request.description = request.POST.get('description')
        priorityID = request.POST.get('priority')
        save_request.priority = PriorityModel.objects.get(id = priorityID)
        save_request.status = maintenance_status
        save_request.image = request.FILES.get('image', None)
        save_request.save()
        messages.success(request,'Maintenance succesfully created') 
        return redirect('request-details', save_request.id)

    context ={
        "priorityStatus" : priorityStatus
    }
    return render(request,'Requests/request_form.html',context)

# Request Details View 
def RequestDetails(request,id):
    maintenance = MaintenanceRequest.objects.get(id = id)
    request_owners = maintenance.owners.all()

    # form data 
    vendors = VendorModel.objects.all()
    list_owners = OwnerModel.objects.all()
    managers = ManagerModel.objects.all()

    # Assign Maintenance Request to Manager
    if request.method == 'POST' and 'add_manager' in request.POST:
        managerID = request.POST.get('managerID')
        managerProfile = ManagerModel.objects.get(id = managerID)
        save_manager = MaintenanceRequest.objects.get(id = id)
        save_manager.assigned_manager = managerProfile
        save_manager.save()
        messages.success(request,'Manager Assigned Maintenance Request') 
        return redirect('request-details', id)
    
    # Remove Manager from Maintenance Request
    if request.method == 'POST' and 'remove_manager' in request.POST:
        managerID = request.POST.get('managerID')
        managerProfile = ManagerModel.objects.get(id = managerID)
        remove_manager = MaintenanceRequest.objects.get(id = id)
        remove_manager.assigned_manager = None
        remove_manager.save()
        messages.success(request,'Manager Removed') 
        return redirect('request-details', id)

    # Assign Maintenance Request to Vendor
    if request.method == 'POST' and 'add_vendor' in request.POST:
        vendorID = request.POST.get('vendorID')
        vendorProfile = VendorModel.objects.get(id = vendorID)
        save_vendor = MaintenanceRequest.objects.get(id = id)
        save_vendor.vendor = vendorProfile
        save_vendor.save()
        messages.success(request,'Vendor Assigned Maintenance Request') 
        return redirect('request-details', id)
    
    # Remove Vendor from Maintenance Request
    if request.method == 'POST' and 'remove_vendor' in request.POST:
        vendorID = request.POST.get('vendorID')
        vendorProfile = VendorModel.objects.get(id = vendorID)
        remove_vendor = MaintenanceRequest.objects.get(id = id)
        remove_vendor.vendor = None
        remove_vendor.save()
        messages.success(request,'Vendor Removed') 
        return redirect('request-details', id)
    

     # Associate Request with Owner
    if request.method == 'POST' and 'add_owners' in request.POST:
        owners_ids = request.POST.getlist('ownersIDs')
        for i in owners_ids:
            # add owner
            save_owner = MaintenanceRequest.objects.get(id = id)
            ownerProfile = OwnerModel.objects.get(id = i)
            save_owner.owners.add(ownerProfile)
        messages.success(request,'Owner added') 
        return redirect('request-details', id)
    
    # Remove Owner from Request
    if request.method == 'POST' and 'remove_owner' in request.POST:
        owner_ID = request.POST.get('owner_ID')
        remove_owner = MaintenanceRequest.objects.get(id = id)
        ownerProfile = OwnerModel.objects.get(id = owner_ID)
        remove_owner.owners.remove(ownerProfile)
        messages.success(request,'Owner Removed') 
        return redirect('request-details', id)
        

    context = {
        "maintenance" : maintenance,
        "request_owners" : request_owners,
        "vendors" : vendors,
        "list_owners" : list_owners,
        "managers" : managers
    }
    return render(request,'Requests/request_details.html',context)
