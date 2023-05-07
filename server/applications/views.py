from django.shortcuts import render,redirect
from django.contrib import messages
import random
from .models import ApplicationModel

from accounts.models import UserModel
from managers.models import ManagerModel
from property.models import PropertyModel


# Create your views here.
def CreateApplication(request, id=None ):
    users = UserModel.objects.all() 

    # update Owner Profile 
    if id is not None:
        applicant = ApplicationModel.objects.get(id=id)
        update = 'active'
        if request.method == 'POST' and 'update_application' in request.POST:
            updateApplication = ApplicationModel.objects.get(id=id)
            userSelect = request.POST.get('userSelect') 
            if userSelect != 'Select User':
                getUser = UserModel.objects.get(id = userSelect)
                updateApplication.user = getUser
            updateApplication.application_type = request.POST.get('applicationType')
            updateApplication.first_name = request.POST.get('firstName')
            updateApplication.last_name = request.POST.get('LastName')
            updateApplication.phone = request.POST.get('Phone')
            updateApplication.email = request.POST.get('Email') 
            updateApplication.street = request.POST.get('Street') 
            updateApplication.town = request.POST.get('Town') 
            updateApplication.city = request.POST.get('City')
            updateApplication.province = request.POST.get('Province') 
            updateApplication.postal_code = request.POST.get('Postal_code') 
            updateApplication.application_number = random.randrange(0, 1000000)
            updateApplication.save()
            messages.success(request,'Application Updated')
            return redirect('application-details', id) 
    
        context = {
            "users" : users,
            "applicant" : applicant,
            "update" : update
        }
        
        return render(request,'applications/create_application.html',context)
    else:
        if request.method == 'POST' and 'create_application' in request.POST:
            saveApplication = ApplicationModel()
            userSelect = request.POST.get('userSelect') 
            if userSelect != 'Select User':
                getUser = UserModel.objects.get(id = userSelect)
                saveApplication.user = getUser
            saveApplication.application_type = request.POST.get('applicationType')
            saveApplication.first_name = request.POST.get('firstName')
            saveApplication.last_name = request.POST.get('LastName')
            saveApplication.phone = request.POST.get('Phone')
            saveApplication.email = request.POST.get('Email') 
            saveApplication.street = request.POST.get('Street') 
            saveApplication.town = request.POST.get('Town') 
            saveApplication.city = request.POST.get('City')
            saveApplication.province = request.POST.get('Province') 
            saveApplication.postal_code = request.POST.get('Postal_code') 
            saveApplication.application_number = random.randrange(0, 1000000)
            saveApplication.save()
            messages.success(request,'Application Created') 
            # redirect if statement 
            if saveApplication.application_type == 'Rental':
                return redirect('rentals')
            else:
                return redirect('buyers')
    
        context = {
            "users" : users
        }
        
        return render(request,'applications/create_application.html',context)

def ApplicationDetails(request,id):
    applicant = ApplicationModel.objects.get(id = id)
    applicant_managers = applicant.management.all()
    managers = ManagerModel.objects.all()
    properties = PropertyModel.objects.filter(property_applications = applicant)

    # Associate Owner with Manager
    if request.method == 'POST' and 'save_applicant_manager' in request.POST:
        managers_ids = request.POST.getlist('manager_id')
        for i in managers_ids:
            # add manager 
            applicantManager = ApplicationModel.objects.get(id = id)
            managerProfile = ManagerModel.objects.get(id = i)
            applicantManager.management.add(managerProfile)
        messages.success(request,'Managers added') 
        return redirect('application-details', id)
    
    # Remove Manager from Applicant
    if request.method == 'POST' and 'delete_applicant_manager' in request.POST:
        managerID = request.POST.get('managerID')
        applicantID = ApplicationModel.objects.get(id = id)
        managerProfile = ManagerModel.objects.get(id = managerID)
        applicantID.management.remove(managerProfile)
        messages.success(request,'Manager Removed') 
        return redirect('application-details', id)

    context = {
        "applicant" : applicant,
        "applicant_managers" : applicant_managers,
        "managers" : managers,
        "properties" : properties
    }
    return render(request,'applications/application_details.html',context)

# Rentals Views 
def RentalApplications(request):
    rentals = ApplicationModel.objects.filter(application_type = 'Rental')

    context = {
        "rentals" : rentals
    }
    return render(request,'Rental/rentals_list.html',context)


# Buyers Views 
def BuyerApplications(request):
    buyers = ApplicationModel.objects.filter(application_type = 'Buyer')

    context = {
        "buyers" : buyers
    }
    return render(request,'Buyer/buyers_list.html',context)