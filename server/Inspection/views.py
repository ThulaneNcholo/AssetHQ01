from django.shortcuts import render,redirect
from django.contrib import messages
from property.models import PropertyModel
from managers.models import ManagerModel
from owners.models import OwnerModel
from Vendors.models import VendorModel
from applications.models import ApplicationModel
import random

# Inspection Models 
from .models import *

# Create your views here.

# create new inspection 
def CreateInspection(request,id):
    inspection = InspectionModel.objects.get(id=id)
    room_inspections = RoomModel.objects.filter(inspectionID = inspection)
    inspection_items = ItemModel.objects.all()
    inspection_images = PhotoModel.objects.all()
    inspector = ManagerModel.objects.get(id = 1)


    context = {
        "inspector" : inspector,
        "inspection" : inspection,
        "room_inspections" : room_inspections,
        "inspection_items" : inspection_items,
        "inspection_images" : inspection_images
    }
    return render(request,'inspection/create_inspection.html',context)

def ShareInspection(request,id):
    inspection = InspectionModel.objects.get(id=id)
    inspector = ManagerModel.objects.get(id = 1)
    shared_managers = inspection.managers.all()
    shared_owners = inspection.owners.all()
    shared_vendors = inspection.vendors.all()

    # forms data 
    list_managers = ManagerModel.objects.all()
    list_owners = OwnerModel.objects.all()
    list_vendors = VendorModel.objects.all()
    list_tenants = ApplicationModel.objects.filter()

    # share with managers post method 
    if request.method == 'POST' and 'add_inspection_managers' in request.POST:
        managers_ids = request.POST.getlist('managerID')
        for i in managers_ids:
            managerProfile = ManagerModel.objects.get(id = i)
            inspection.managers.add(managerProfile)
        messages.success(request,'Managers added') 
        return redirect('share-inspection', id)
    
    # share with owners post method 
    if request.method == 'POST' and 'add_inspection_owners' in request.POST:
        ownerID = request.POST.getlist('ownerID')
        for i in ownerID:
            ownerProfile = OwnerModel.objects.get(id =i)
            inspection.owners.add(ownerProfile)
        messages.success(request,'Owners added') 
        return redirect('share-inspection', id)
    
    # share with Vendor post method 
    if request.method == 'POST' and 'add_inspection_vendor' in request.POST:
        vendorID = request.POST.getlist('vendorID')
        for i in vendorID:
            vendorProfile = VendorModel.objects.get(id = i)
            inspection.vendors.add(vendorProfile)
        messages.success(request,'Vendors added') 
        return redirect('share-inspection', id)
    

    # Remove Methods start 
    # remove managers 
    if request.method == 'POST' and 'delete-manager' in request.POST:
        managerID = request.POST.get('managerID')
        managerProfile = ManagerModel.objects.get(id = managerID)
        inspection.managers.remove(managerProfile)
        messages.success(request,'Manager Removed Successfully') 
        return redirect('share-inspection', id)
    
    # remove owners 
    if request.method == 'POST' and 'delete-owner' in request.POST:
        ownerID = request.POST.get('ownerID')
        ownerProfile = OwnerModel.objects.get(id = ownerID)
        inspection.owners.remove(ownerProfile)
        messages.success(request,'Owner Removed Successfully') 
        return redirect('share-inspection', id)
    
    # remove vendors 
    if request.method == 'POST' and 'delete-vendor' in request.POST:
        vendorID = request.POST.get('vendorID')
        vendorProfile = VendorModel.objects.get(id = vendorID)
        inspection.vendors.remove(vendorProfile)
        messages.success(request,'Vendor Removed Successfully') 
        return redirect('share-inspection', id)

    context = {
        "inspector" : inspector,
        "list_managers" : list_managers,
        "list_owners" : list_owners,
        "list_vendors" : list_vendors,
        "inspection" : inspection,
        "shared_managers" : shared_managers,
        "shared_owners" : shared_owners,
        "shared_vendors" : shared_vendors
    }
    return render(request,'inspection/share_inspection.html',context)

# Inspection Form 
def InspectionForm(request,id):
    property = PropertyModel.objects.get(id =id)
    inspector = ManagerModel.objects.get(id = 1)

    # create inspection post method 
    if request.method == 'POST' and 'submit_inspection' in request.POST:
        # save Inspection Model  
        inspection = InspectionModel.objects.create(inspection_number= random.randrange(0, 1000000), property=property , inspector=inspector)
        # save room Model 
        room = RoomModel.objects.create(name=request.POST.get('room'),comments=request.POST.get('Comments'))
        room.inspectionID.add(inspection)
        # save item model 
        item = ItemModel.objects.create(name=request.POST.get('item_name'), description=request.POST.get('item_description'), room=room)
        # save images model 
        images = PhotoModel.objects.create(image1=request.FILES.get('image1', None), image2=request.FILES.get('image2', None), image3=request.FILES.get('image3', None), item=item)
        return redirect('create-inspections', inspection.id)

    return render(request,'inspection/inspection_form.html')

# list all inspections 
def ListInspections(request):
    properties = PropertyModel.objects.all()
    inspections = InspectionModel.objects.all()

    context = {
        "inspections" : inspections,
        "properties" : properties
    }
    return render(request,'inspection/list_inspections.html',context)


# add inspection from inspection id 
def AddInspectionForm(request,id):
    inspection = InspectionModel.objects.get(id = id)

    # create inspection post method 
    if request.method == 'POST' and 'add_inspection' in request.POST:
        # save room Model 
        room = RoomModel.objects.create(name=request.POST.get('room'),comments=request.POST.get('Comments'))
        room.inspectionID.add(inspection)
        # save item model 
        item = ItemModel.objects.create(name=request.POST.get('item_name'), description=request.POST.get('item_description'), room=room)
        # save images model 
        images = PhotoModel.objects.create(image1=request.FILES.get('image1', None), image2=request.FILES.get('image2', None), image3=request.FILES.get('image3', None), item=item)
        return redirect('create-inspections', inspection.id)

    context ={
        "inspection" : inspection
    }

    return render(request,'inspection/add_inspection_ID.html',context)






