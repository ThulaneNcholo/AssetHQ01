from django.shortcuts import render,redirect
from django.contrib import messages 
import random
from .models import *
from property.models import PropertyModel

# Create your views here.
def TaskList(request):
    properties = PropertyModel.objects.all()

    # Task Models 
    openStatus = TaskStatusModel.objects.get(name = 'Open')
    open_tasks = TaskModel.objects.filter(status = openStatus)
    # progress Task 
    progressStatus = TaskStatusModel.objects.get(name = 'In Progress')
    progress_tasks = TaskModel.objects.filter(status = progressStatus)
    # complete Task 
    completeStatus = TaskStatusModel.objects.get(name = 'Completed')
    complete_tasks = TaskModel.objects.filter(status = completeStatus)

    if request.method == 'POST' and 'selected_property' in request.POST:
        PropertyID = request.POST.get('Property_ID')
        # store property ID to be used in other views
        request.session['property_id'] = PropertyID
        return redirect('add-task')

    context = {
        "properties" : properties,
        "open_tasks" : open_tasks,
        "progress_tasks" : progress_tasks,
        'complete_tasks' : complete_tasks
    }

    return render(request,'Tasks/task-list.html',context)


# add Task View 
def AddTask(request,id=None):
    if id is not None:
        propertyID = id
        propertyProfile = PropertyModel.objects.get(id = propertyID)
        task_status_open = TaskStatusModel.objects.get(name = 'Open')

        manager = ManagerModel.objects.get(id = 1)

        if request.method == 'POST' and 'add_task' in request.POST:
            save_task = TaskModel()
            save_task.task_number = random.randrange(0, 1000000)
            save_task.property = propertyProfile
            save_task.created_by = manager
            save_task.due_date = request.POST.get('due_date')
            save_task.title = request.POST.get('title')
            save_task.description = request.POST.get('description')
            save_task.status = task_status_open
            save_task.save()
            messages.success(request,'Task successfully created')
            return redirect('view-task',save_task.id) 

        context = {
            "propertyProfile" : propertyProfile
        }

        return render(request,'Tasks/add_task.html',context)

    else:
        propertyID = request.session.get('property_id')
        propertyProfile = PropertyModel.objects.get(id = propertyID)
        task_status_open = TaskStatusModel.objects.get(name = 'Open')

        manager = ManagerModel.objects.get(id = 1)

        if request.method == 'POST' and 'add_task' in request.POST:
            save_task = TaskModel()
            save_task.task_number = random.randrange(0, 1000000)
            save_task.property = propertyProfile
            save_task.created_by = manager
            save_task.due_date = request.POST.get('due_date')
            save_task.title = request.POST.get('title')
            save_task.description = request.POST.get('description')
            save_task.status = task_status_open
            save_task.save()
            messages.success(request,'Task successfully created')
            return redirect('view-task',save_task.id) 

        context = {
            "propertyProfile" : propertyProfile
        }

        return render(request,'Tasks/add_task.html',context)

def ViewTask(request,id):
    task = TaskModel.objects.get(id = id)
    task_managers = task.managers.all()
    task_owners = task.owners.all()

    # Form data 
    managers = ManagerModel.objects.all()
    ownersModal = OwnerModel.objects.all()

    # Associate Task with Manager
    if request.method == 'POST' and 'add_owner_manager' in request.POST:
        managers_ids = request.POST.getlist('manager_id')
        for i in managers_ids:
            # add manager 
            taskProfile = TaskModel.objects.get(id = id)
            managerProfile = ManagerModel.objects.get(id = i)
            taskProfile.managers.add(managerProfile)
        messages.success(request,'Managers added') 
        return redirect('view-task', id)
    
    # Remove Manager from Task
    if request.method == 'POST' and 'delete-manager' in request.POST:
        managerID = request.POST.get('managerID')
        taskProfile = TaskModel.objects.get(id = id)
        managerProfile = ManagerModel.objects.get(id = managerID)
        taskProfile.managers.remove(managerProfile)
        messages.success(request,'Manager Removed') 
        return redirect('view-task', id)
    
    # Associate Task with Owner
    if request.method == 'POST' and 'add_owner' in request.POST:
        owners_ids = request.POST.getlist('ownerID')
        for i in owners_ids:
            # add owner
            taskProfile = TaskModel.objects.get(id = id)
            ownerProfile = OwnerModel.objects.get(id = i)
            taskProfile.owners.add(ownerProfile)
        messages.success(request,'Owner added') 
        return redirect('view-task', id)
    
    # Remove Owner from Task
    if request.method == 'POST' and 'remove_owner' in request.POST:
        owner_ID = request.POST.get('owner_ID')
        taskProfile = TaskModel.objects.get(id = id)
        ownerProfile = OwnerModel.objects.get(id = owner_ID)
        taskProfile.owners.remove(ownerProfile)
        messages.success(request,'Owner Removed') 
        return redirect('view-task', id)
    

    # Task Status 
    if request.method == 'POST' and 'open_task' in request.POST:
        task_status_open = TaskStatusModel.objects.get(name = 'Open')
        save_open = TaskModel.objects.get(id = id)
        save_open.status = task_status_open
        save_open.save()
        messages.success(request,'Task Open')
        return redirect('view-task', id)
    
    if request.method == 'POST' and 'progress_task' in request.POST:
        task_status_progress = TaskStatusModel.objects.get(name = 'In Progress')
        save_progress = TaskModel.objects.get(id = id)
        save_progress.status = task_status_progress
        save_progress.save()
        messages.success(request,'Task in progress')
        return redirect('view-task', id)
    
    if request.method == 'POST' and 'complete_task' in request.POST:
        task_status_complete = TaskStatusModel.objects.get(name = 'Completed')
        save_complete = TaskModel.objects.get(id = id)
        save_complete.status = task_status_complete
        save_complete.save()
        messages.success(request,'Task Complete')
        return redirect('view-task', id)

    context = {
        "task" : task,
        "task_managers" : task_managers,
        "task_owners" : task_owners,
        "managers" : managers,
        "ownersModal" : ownersModal,
        
    }
    return render(request,'Tasks/task_details.html',context)