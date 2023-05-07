from django.shortcuts import render,redirect
from django.contrib import messages 
import random
from .models import OwnerModel,OwnerManagement
from accounts.models import UserModel
from managers.models import ManagerModel

# Create your views here.

# list all owners 
def OwnersList(request):
    owners = OwnerModel.objects.all()

    context = {
        "owners" : owners
    }

    return render(request,'owners/list_owners.html',context)

# Create new Owner 
def CreateOwner(request,id=None ):
    users = UserModel.objects.all()

    # update Owner Profile 
    if id is not None:
        owner = OwnerModel.objects.get(id=id)
        update = 'active'

        if request.method == 'POST' and 'update_owner' in request.POST:
            updateOwner = OwnerModel.objects.get(id=id)
            updateOwner.first_name = request.POST.get('firstName')
            updateOwner.last_name = request.POST.get('LastName')
            updateOwner.phone = request.POST.get('Phone')
            updateOwner.email = request.POST.get('Email') 
            updateOwner.street = request.POST.get('Street') 
            updateOwner.town = request.POST.get('Town') 
            updateOwner.city = request.POST.get('City')
            updateOwner.province = request.POST.get('Province') 
            updateOwner.postal_code = request.POST.get('Postal_code') 
            # updateOwner.profile_pic = request.FILES['Coverimage']
            updateOwner.save()
            messages.success(request,'Owner Updated') 
            return redirect('owners-details', id)
        
        context = {
            "users" : users,
            "owner" : owner,
            "update" : update
        }

        return render(request,'owners/add_owner.html',context)
    else:
        # Create New Owner
        if request.method == 'POST' and 'create_owner' in request.POST:
            saveOwner = OwnerModel()
            userSelect = request.POST.get('userSelect')
            if userSelect != 'Select User':
                getUser = UserModel.objects.get(id = userSelect)
                saveOwner.user = getUser
            saveOwner.first_name = request.POST.get('firstName')
            saveOwner.last_name = request.POST.get('LastName')
            saveOwner.phone = request.POST.get('Phone')
            saveOwner.email = request.POST.get('Email') 
            saveOwner.street = request.POST.get('Street') 
            saveOwner.town = request.POST.get('Town') 
            saveOwner.city = request.POST.get('City')
            saveOwner.province = request.POST.get('Province') 
            saveOwner.postal_code = request.POST.get('Postal_code') 
            saveOwner.profile_pic = request.FILES['Coverimage']
            saveOwner.owner_id = random.randrange(0, 1000000)
            saveOwner.save()
            messages.success(request,'new owner created') 
            return redirect('owners')
        
        context = {
            "users" : users
        }

        return render(request,'owners/add_owner.html',context)


# Owner Details 
def OwnerDetails(request,id):
    owner = OwnerModel.objects.get(id = id)
    owner_management = owner.management.all()
    managers = ManagerModel.objects.all()

    # Associate Owner with Manager
    if request.method == 'POST' and 'add_owner_manager' in request.POST:
        managers_ids = request.POST.getlist('manager_id')
        for i in managers_ids:
            # add manager 
            ownerID = OwnerModel.objects.get(id = id)
            managerProfile = ManagerModel.objects.get(id = i)
            ownerID.management.add(managerProfile)
        messages.success(request,'Managers added') 
        return redirect('owners-details', id)
    

    # Remove Manager from Owner
    if request.method == 'POST' and 'delete-manager' in request.POST:
        managerID = request.POST.get('managerID')
        ownerID = OwnerModel.objects.get(id = id)
        managerProfile = ManagerModel.objects.get(id = managerID)
        ownerID.management.remove(managerProfile)
        messages.success(request,'Manager Removed') 
        return redirect('owners-details', id)

    context = {
        "owner" : owner,
        "owner_management" : owner_management,
        "managers" : managers
    }
    return render(request,'owners/owner_details.html',context)
