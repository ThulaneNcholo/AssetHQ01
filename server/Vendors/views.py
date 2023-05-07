from django.shortcuts import render,redirect
from django.contrib import messages 
import random
from .models import VendorModel,VendorServices

# Create your views here.

# list Vendors 
def AddVendor(request):

    # add vendor post method 
    if request.method == 'POST' and 'add_vendor' in request.POST:
        save_vendor = VendorModel()
        save_vendor.vendor_id = random.randrange(0, 1000000)
        save_vendor.company_name = request.POST.get('compnay_name')
        save_vendor.first_name = request.POST.get('first_name')
        save_vendor.last_name = request.POST.get('last_name')
        save_vendor.email = request.POST.get('email')
        save_vendor.phone = request.POST.get('phone')
        save_vendor.street = request.POST.get('Street')
        save_vendor.town = request.POST.get('town')
        save_vendor.city = request.POST.get('City')
        save_vendor.province = request.POST.get('Province')
        save_vendor.postal_code = request.POST.get('postal_code')
        save_vendor.cover_image = request.FILES.get('coverImage', None) 
        save_vendor.save()
        return redirect('vendor-view', save_vendor.id)

    return render(request,'Vendors/add_vendor.html')

# View Vendor 
def VendorView(request,id):
    vendorData = VendorModel.objects.get(id = id)
    venderServicesData = vendorData.vendor_services.all()

    # add vendor post method 
    if request.method == 'POST' and 'submit_service' in request.POST:
        name = request.POST.get('service_name')
        add_service = VendorServices()
        add_service.name = name
        add_service.save()

        # add service to vendor model 
        vendorSave = VendorModel.objects.get(id = id)
        vendorServiceField = VendorServices.objects.get(id = add_service.id)
        vendorSave.vendor_services.add(vendorServiceField)
        messages.success(request,'New Service Successfully Added')
        return redirect('vendor-view',id)
    
    # add vendor post method 
    if request.method == 'POST' and 'remove_service' in request.POST:
        serviceID = request.POST.get('serviceID')
        removeService = VendorModel.objects.get(id = id)
        vendorProfile = VendorServices.objects.get(id = serviceID)
        removeService.vendor_services.remove(vendorProfile)
        messages.success(request,'Service Removed')
        return redirect('vendor-view',id)

    context = {
        "vendorData" : vendorData,
        "venderServicesData" : venderServicesData
    }
    return render(request,'Vendors/vendor-view.html',context)


# add Vendors Services 
def AddVendorService(request,id):
    return render(request,'Vendors/service-list.html')

# list Vendors 
def VendorList(request):
    vendorListData = VendorModel.objects.all()

    context = {
        "vendorListData" : vendorListData
    }
    return render(request,'Vendors/vendor_list.html',context)


