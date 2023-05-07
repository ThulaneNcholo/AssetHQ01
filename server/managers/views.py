from django.shortcuts import render,redirect
from django.contrib import messages
import random
from .models import ManagerModel

from accounts.models import UserModel

# Create your views here.

# add manager view 
def AddManager(request, id=None):
    users = UserModel.objects.all() 

    
    # Update Manager
    if id is not None:
        manager = ManagerModel.objects.get(id = id)
        update = 'active'

        if request.method == 'POST' and 'update_manager' in request.POST:
            # save manager start 
            updateManager = ManagerModel.objects.get(id = id)
            updateManager.first_name = request.POST.get('firstName')
            updateManager.last_name = request.POST.get('LastName')
            updateManager.phone = request.POST.get('Phone')
            updateManager.email = request.POST.get('Email') 
            updateManager.street = request.POST.get('Street') 
            updateManager.town = request.POST.get('Town') 
            updateManager.city = request.POST.get('City')
            updateManager.province = request.POST.get('Province') 
            updateManager.postal_code = request.POST.get('Postal_code') 
            # updateManager.profile_pic = request.FILES['Coverimage'] 
            updateManager.save()
            messages.success(request,'Manager Updated') 
            return redirect('manager-details', id)

        context = {
            "manager" : manager,
            "update" : update
        }

        return render(request,'managers/add_manager.html',context)

    # create manager 
    else:
        if request.method == 'POST' and 'create_manager' in request.POST:
            userSelect = request.POST.get('userSelect') 
            getUser = UserModel.objects.get(id = userSelect)
            # save manager start 
            saveManager = ManagerModel()
            saveManager.user = getUser
            saveManager.first_name = request.POST.get('firstName')
            saveManager.last_name = request.POST.get('LastName')
            saveManager.phone = request.POST.get('Phone')
            saveManager.email = request.POST.get('Email') 
            saveManager.street = request.POST.get('Street') 
            saveManager.town = request.POST.get('Town') 
            saveManager.city = request.POST.get('City')
            saveManager.province = request.POST.get('Province') 
            saveManager.postal_code = request.POST.get('Postal_code') 
            saveManager.profile_pic = request.FILES['Coverimage']
            saveManager.manager_number = random.randrange(0, 1000000)
            saveManager.save()
            messages.success(request,'new manager created') 
            return redirect('managers')
    
        context = {
            "users" : users
        }

        return render(request,'managers/add_manager.html',context)

# List all Managers 
def ManagersList(request):
    managers = ManagerModel.objects.all()

    context = {
        "managers" : managers
    }
    return render(request,'managers/managers_list.html',context)

# Manager Details 
def ManagerDetails(request,id):
    manager = ManagerModel.objects.get(id = id)

    context = {
        "manager" : manager
    }
    return render(request,'managers/manager_details.html',context)
