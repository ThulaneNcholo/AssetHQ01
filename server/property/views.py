from django.shortcuts import render,redirect
from django.contrib import messages 
import random
from datetime import date
from django.db.models import Q
from django.db.models import Sum
from django.db.models import Case, When

from .models import *

from managers.models import ManagerModel
from owners.models import OwnerModel
from applications.models import ApplicationModel
from Tasks.models import *
from Inspection.models import *
from Documents.models import *
from Requests.models import *
from Financials.models import *


# Create your views here.
def AddProperty(request):
    propertyFor = PropertyForModel.objects.all()
    propertyType = PropertyTypeModel.objects.all()
    eletricityType = EletricityModel.objects.all()

    if request.method == 'POST' and 'add_property' in request.POST:
        create_property  = PropertyModel()
        create_property.propertyName = request.POST.get('Property_Name')
        create_property.bedrooms = request.POST.get('Bedrooms')
        create_property.bathrooms = request.POST.get('Bathrooms')
        create_property.garage = request.POST.get('Garages')
        create_property.Floor_Size = request.POST.get('floor_size')
        create_property.Erf_Size = request.POST.get('erf_size')
        create_property.Description = request.POST.get('description')
        create_property.street = request.POST.get('Street')
        create_property.town = request.POST.get('town')
        create_property.city = request.POST.get('City')
        create_property.province = request.POST.get('Province')
        create_property.postal_code = request.POST.get('postal_code')
        create_property.coverImage = request.FILES.get('coverImage', None) 
        create_property.image1 = request.FILES.get('image1', None) 
        create_property.image2 = request.FILES.get('image2', None) 
        create_property.image3 = request.FILES.get('image3', None) 
        create_property.listing_number = random.randrange(0, 1000000)
        # ForeignKey fields Entries 
        create_property.property_for = PropertyForModel.objects.get(id=request.POST.get('property_for')) 
        create_property.property_type = PropertyTypeModel.objects.get(id=request.POST.get('property_type')) 
        create_property.eletricity_type = EletricityModel.objects.get(id=request.POST.get('eletricity_type')) 
        create_property.save()
        messages.success(request,'Property Successfully Created') 
        return redirect('properties')
    
    context = {
        "property_For" : propertyFor,
        "property_type" : propertyType,
        "eletricity_type" : eletricityType
    }
        
    return render(request,'property/add_property.html',context)


def PropertiesView(request):
    properties = PropertyModel.objects.all()

    context = {
        "properties" : properties
    }

    return render(request,'property/properties.html', context)

def PropertyDetails(request,id):
    property = PropertyModel.objects.get(id = id)
    property_managers = property.managers.all()
    property_owners = property.owners.all()
    property_features = property.features_property.all()
    managers = ManagerModel.objects.all()
    ownersModal = OwnerModel.objects.all()
    features = PropertyFeatures.objects.all()
    # Open Tasks Models Count 
    openStatus = TaskStatusModel.objects.get(name = 'Open')
    open_task_count = TaskModel.objects.filter(Q(status = openStatus) & Q(property=property)).count()
    # maintenance count 
    maintenance_pending = MaintenanceStatusModel.objects.get(name = 'Pending')
    maintenance_count = MaintenanceRequest.objects.filter(Q(status = maintenance_pending) & Q(property=property)).count()

    # Associate Property with Manager
    if request.method == 'POST' and 'add_owner_manager' in request.POST:
        managers_ids = request.POST.getlist('manager_id')
        for i in managers_ids:
            # add manager 
            propertyID = PropertyModel.objects.get(id = id)
            managerProfile = ManagerModel.objects.get(id = i)
            propertyID.managers.add(managerProfile)
        messages.success(request,'Managers added') 
        return redirect('propert-details', id)
    

    # Remove Manager from Property
    if request.method == 'POST' and 'delete-manager' in request.POST:
        managerID = request.POST.get('managerID')
        propertyID = PropertyModel.objects.get(id = id)
        managerProfile = ManagerModel.objects.get(id = managerID)
        propertyID.managers.remove(managerProfile)
        messages.success(request,'Manager Removed') 
        return redirect('propert-details', id)
    

    # Associate Property with Owner
    if request.method == 'POST' and 'add_owner' in request.POST:
        owners_ids = request.POST.getlist('ownerID')
        for i in owners_ids:
            # add owner
            propertyID = PropertyModel.objects.get(id = id)
            ownerProfile = OwnerModel.objects.get(id = i)
            propertyID.owners.add(ownerProfile)
        messages.success(request,'Owner added') 
        return redirect('propert-details', id)
    
    # Remove Owner from Property
    if request.method == 'POST' and 'remove_owner' in request.POST:
        owner_ID = request.POST.get('owner_ID')
        propertyID = PropertyModel.objects.get(id = id)
        ownerProfile = OwnerModel.objects.get(id = owner_ID)
        propertyID.owners.remove(ownerProfile)
        messages.success(request,'Owner Removed') 
        return redirect('propert-details', id)
    
    # Add Property Features
    if request.method == 'POST' and 'save_features' in request.POST:
        FeatureIDs = request.POST.getlist('FeatureID')
        propertyID = PropertyModel.objects.get(id=id)
        for i in FeatureIDs:
            feature_id = PropertyFeatures.objects.get(id=i)
            if not propertyID.features_property.filter(id=feature_id.id).exists():
                propertyID.features_property.add(feature_id)
        messages.success(request, 'Features added') 
        return redirect('propert-details', id)
    
    # Remove Feature From Property
    if request.method == 'POST' and 'remove_feature' in request.POST:
        modal_feature = request.POST.get('feature_modal_id')
        propertyID = PropertyModel.objects.get(id=id)
        featureID = PropertyFeatures.objects.get(id = modal_feature)
        propertyID.features_property.remove(featureID)
        messages.success(request,'Feature Removed') 
        return redirect('propert-details', id)
    
    

    context = {
        "property" : property,
        "property_managers" : property_managers,
        "property_owners" : property_owners,
        "property_features" : property_features,
        "managers" : managers,
        "ownersModal" : ownersModal,
        "features" : features,
        "open_task_count" : open_task_count,
        "maintenance_count" : maintenance_count
    }
    return render(request,'property/property_details.html',context)

def ViewProperty(request,id):
    property = PropertyModel.objects.get(id = id)

    # Associate Property with Manager
    if request.method == 'POST' and 'add_owner_manager' in request.POST:
        managers_ids = request.POST.getlist('manager_id')
        for i in managers_ids:
            # add manager 
            propertyID = PropertyModel.objects.get(id = id)
            managerProfile = ManagerModel.objects.get(id = i)
            propertyID.managers.add(managerProfile)
        messages.success(request,'Managers added') 
        return redirect('view-property', id)
    

    # Remove Manager from Property
    if request.method == 'POST' and 'delete-manager' in request.POST:
        managerID = request.POST.get('managerID')
        propertyID = PropertyModel.objects.get(id = id)
        managerProfile = ManagerModel.objects.get(id = managerID)
        propertyID.managers.remove(managerProfile)
        messages.success(request,'Manager Removed') 
        return redirect('view-property', id)
    

    # Associate Property with Owner
    if request.method == 'POST' and 'add_owner' in request.POST:
        owners_ids = request.POST.getlist('ownerID')
        for i in owners_ids:
            # add owner
            propertyID = PropertyModel.objects.get(id = id)
            ownerProfile = OwnerModel.objects.get(id = i)
            propertyID.owners.add(ownerProfile)
        messages.success(request,'Owner added') 
        return redirect('view-property', id)
    
    # Remove Owner from Property
    if request.method == 'POST' and 'remove_owner' in request.POST:
        owner_ID = request.POST.get('owner_ID')
        propertyID = PropertyModel.objects.get(id = id)
        ownerProfile = OwnerModel.objects.get(id = owner_ID)
        propertyID.owners.remove(ownerProfile)
        messages.success(request,'Owner Removed') 
        return redirect('view-property', id)
    
    # Add Property Features
    if request.method == 'POST' and 'save_features' in request.POST:
        FeatureIDs = request.POST.getlist('FeatureID')
        propertyID = PropertyModel.objects.get(id=id)
        for i in FeatureIDs:
            feature_id = PropertyFeatures.objects.get(id=i)
            if not propertyID.features_property.filter(id=feature_id.id).exists():
                propertyID.features_property.add(feature_id)
        messages.success(request, 'Features added') 
        return redirect('view-property', id)
    
    # Remove Feature From Property
    if request.method == 'POST' and 'remove_feature' in request.POST:
        modal_feature = request.POST.get('feature_modal_id')
        propertyID = PropertyModel.objects.get(id=id)
        featureID = PropertyFeatures.objects.get(id = modal_feature)
        propertyID.features_property.remove(featureID)
        messages.success(request,'Feature Removed') 
        return redirect('view-property', id)
    

    context = {
        "property" : property
    }
    return render(request,'property/view_property.html',context)

def ContentOne(request,id):
    property = PropertyModel.objects.get(id = id)
    property_managers = property.managers.all()
    property_owners = property.owners.all()
    property_features = property.features_property.all()
    managers = ManagerModel.objects.all()
    ownersModal = OwnerModel.objects.all()
    features = PropertyFeatures.objects.all()

    context = {
        "property" : property,
        "property_managers" : property_managers,
        "property_owners" : property_owners,
        "property_features" : property_features,
        "managers" : managers,
        "ownersModal" : ownersModal,
        "features" : features 
    }

    return render(request,'HTMX/content1.html',context)

def ContentTwo(request,id):
    property = PropertyModel.objects.get(id = id)
    property_applicantions = property.property_applications.all()
    applications = ApplicationModel.objects.all()
    applicants = ApplicationModel.objects.all()

    context = {
        "property" : property,
        "applications" : applications,
        "applicants" : applicants,
        "property_applicantions" : property_applicantions
    }
    return render(request,'HTMX/content2.html',context)

def PropertyApplicantsView(request):
    if request.method == 'POST':
        propertyID = request.POST.get('propertyID')
        property = PropertyModel.objects.get(id = propertyID)
        applicationIDS = request.POST.getlist('applicantID')
        for i in applicationIDS:
            applicants = ApplicationModel.objects.get(id=i)
            if not property.property_applications.filter(id=applicants.id).exists():
                property.property_applications.add(applicants)

        property_applicantions = property.property_applications.all()

        context = {
            "property_applicantions" : property_applicantions
        }


    return render(request,'partials/property_applicants.html',context)


# New Views Start 
def PropertyApplications(request,id):
    property = PropertyModel.objects.get(id = id)
    # Open Tasks Models Count 
    openStatus = TaskStatusModel.objects.get(name = 'Open')
    open_task_count = TaskModel.objects.filter(Q(status = openStatus) & Q(property=property)).count()
    # property_tenants = property.tenants.all()
    property_tenants = LeaseModel.objects.filter(property = property)
    # maintenance count 
    maintenance_pending = MaintenanceStatusModel.objects.get(name = 'Pending')
    maintenance_count = MaintenanceRequest.objects.filter(Q(status = maintenance_pending) & Q(property=property)).count()

    # store property ID to be used in other views
    propertyID = id 
    request.session['my_id'] = propertyID

    tenantsID = []
    for i in property_tenants:
        tenantsID.append(i.tenant.id)

    property_applicantions = property.property_applications.exclude(id__in=tenantsID )
    today = date.today()


    # add tenant post method
    if request.method == 'POST' and 'add_tenant' in request.POST:
        applicantID = request.POST.get('applicantID')
        applicantProfile = ApplicationModel.objects.get(id = applicantID)
        # save to tenant model 
        save_tenant = PropertyTenant()
        save_tenant.applicant = applicantProfile
        save_tenant.move_in = request.POST.get('moveIn')
        save_tenant.move_out = request.POST.get('moveOut')
        save_tenant.fee = request.POST.get('price')
        save_tenant.paydate = request.POST.get('agreement')
        save_tenant.save()
        # save to property model 
        property.tenants.add(save_tenant)
        messages.success(request,'New Tenant successfully added') 
        return redirect('applicationsProperty', id)
    
    # add tenant post method
    if request.method == 'POST' and 'edit_tenant' in request.POST:
        applicantID = request.POST.get('applicantID')
        save_tenant_edit = PropertyTenant.objects.get(id = applicantID)

        # check if theres move in date 
        move_in = request.POST.get('moveIn')
        if move_in:
            save_tenant_edit.move_in = request.POST.get('moveIn')
        else:
             save_tenant_edit.move_in = save_tenant_edit.move_in

        # check if theres move out date
        move_out = request.POST.get('moveOut')
        if move_out:
            save_tenant_edit.move_out = request.POST.get('moveOut')
        else:
            save_tenant_edit.move_out = save_tenant_edit.move_out

        save_tenant_edit.fee = request.POST.get('price')
        save_tenant_edit.paydate = request.POST.get('agreement')
        save_tenant_edit.save()
        messages.success(request,'Tenant successfully updated') 
        return redirect('applicationsProperty', id)

    context = {
        "property" : property,
        "property_applicantions" : property_applicantions,
        "property_tenants" : property_tenants,
        "today" : today,
        "open_task_count" : open_task_count,
        "maintenance_count" : maintenance_count
    }
    return render(request,'NewViews/property-applications.html',context)

# Lease View start 
def LeaseView(request,action ,id):
    if action == 'newlease':
        edit = action
        # handle new lease action
        applicant_profile = ApplicationModel.objects.get(id = id)
        #get property ID from session storage
        propertyID = request.session.get('my_id')
        propertyProfile = PropertyModel.objects.get(id = propertyID)

         # create lease agreement post method 
        if request.method == 'POST' and 'create_lease' in request.POST:
            save_lease = LeaseModel()
            save_lease.lease_number = random.randrange(0, 1000000)
            save_lease.tenant = applicant_profile
            save_lease.property  = propertyProfile
            save_lease.start_date = request.POST.get('start_date')
            save_lease.end_date = request.POST.get('end_date')
            save_lease.rent_amount = request.POST.get('rent_amount')
            save_lease.late_fee = request.POST.get('late_fee')
            save_lease.security_deposit = request.POST.get('security_deposit')
            save_lease.payment_schedule = request.POST.get('payment_schedule')
            save_lease.late_payment_policiy = request.POST.get('late_payment_policiy')
            save_lease.utilities = request.POST.get('utilities')
            save_lease.maintenance_responsibilities = request.POST.get('maintenance_responsibilities')
            save_lease.renewal_options = request.POST.get('renewal_options')
            save_lease.subletting_policy = request.POST.get('subletting_policy')
            save_lease.pet_policy = request.POST.get('pet_policy')
            save_lease.save()
            messages.success(request,'Lease successfully created') 
            return redirect('applicationsProperty', id)
        

        context = {
            "applicant_profile" : applicant_profile,
            "propertyProfile" : propertyProfile,
        }
        
        return render(request,'Tenants/lease.html',context)
    elif action == 'editlease':
        edit = action
        # handle edit lease action
        applicant_profile = ApplicationModel.objects.get(id = id)
        #get property ID from session storage
        propertyID = request.session.get('my_id')
        propertyProfile = PropertyModel.objects.get(id = propertyID)
        property_tenant = LeaseModel.objects.get(id = id)

        # create lease agreement post method 
        if request.method == 'POST' and 'edit_lease' in request.POST:
            update_lease = LeaseModel.objects.get(id = id)

            move_in_date = request.POST.get('start_date')
            if move_in_date:
                update_lease.start_date = request.POST.get('start_date')
            else:
                update_lease.start_date = update_lease.start_date

            move_out_date = request.POST.get('end_date')
            if move_out_date:
                update_lease.end_date = request.POST.get('end_date')
            else:
                update_lease.end_date = update_lease.end_date
            
            update_lease.rent_amount = request.POST.get('rent_amount')
            update_lease.late_fee = request.POST.get('late_fee')
            update_lease.security_deposit = request.POST.get('security_deposit')
            update_lease.payment_schedule = request.POST.get('payment_schedule')
            update_lease.late_payment_policiy = request.POST.get('late_payment_policiy')
            update_lease.utilities = request.POST.get('utilities')
            update_lease.maintenance_responsibilities = request.POST.get('maintenance_responsibilities')
            update_lease.renewal_options = request.POST.get('renewal_options')
            update_lease.subletting_policy = request.POST.get('subletting_policy')
            update_lease.pet_policy = request.POST.get('pet_policy')
            update_lease.save()
            messages.success(request,'Lease successfully updated') 
            return redirect('applicationsProperty', propertyProfile.id)
        

        context = {
            "applicant_profile" : applicant_profile,
            "propertyProfile" : propertyProfile,
            "property_tenant" : property_tenant,
            "edit" : edit
        }
        
        return render(request,'Tenants/lease.html',context)
    

# Property Tasks 
def PropertyTasks(request,id):
    property = PropertyModel.objects.get(id = id)

    # Task Models 
    openStatus = TaskStatusModel.objects.get(name = 'Open')
    open_tasks = TaskModel.objects.filter(Q(status = openStatus) & Q(property=property))
    open_task_count = TaskModel.objects.filter(Q(status = openStatus) & Q(property=property)).count()
    # progress Task 
    progressStatus = TaskStatusModel.objects.get(name = 'In Progress')
    progress_tasks = TaskModel.objects.filter(Q(status = progressStatus) & Q(property=property))
    
    # complete Task 
    completeStatus = TaskStatusModel.objects.get(name = 'Completed')
    complete_tasks = TaskModel.objects.filter(Q(status = completeStatus) & Q(property=property))

    # maintenance count 
    maintenance_pending = MaintenanceStatusModel.objects.get(name = 'Pending')
    maintenance_count = MaintenanceRequest.objects.filter(Q(status = maintenance_pending) & Q(property=property)).count()
    

    context = {
        "property" : property,
        "open_tasks" : open_tasks,
        "progress_tasks" : progress_tasks,
        'complete_tasks' : complete_tasks,
        "open_task_count" : open_task_count,
        "maintenance_count" : maintenance_count
    }

    return render(request,'property/property_tasks.html',context)


# Property Inspections 
def PropertyInspections(request,id):
    property = PropertyModel.objects.get(id = id)
    inspections = InspectionModel.objects.filter(property = property)
    # Open Tasks Models Count 
    openStatus = TaskStatusModel.objects.get(name = 'Open')
    open_task_count = TaskModel.objects.filter(Q(status = openStatus) & Q(property=property)).count()
    # maintenance count 
    maintenance_pending = MaintenanceStatusModel.objects.get(name = 'Pending')
    maintenance_count = MaintenanceRequest.objects.filter(Q(status = maintenance_pending) & Q(property=property)).count()

    context = {
        "property" : property,
        "open_task_count" : open_task_count,
        "inspections" : inspections,
        "maintenance_count" : maintenance_count
    }
    return render(request,'property/property_inspections.html',context)

# Property Files 
def PropertyModelFiles(request,id):
    property = PropertyModel.objects.get(id = id)
    properties_files = PropertyDocument.objects.filter(property = property)
    # Open Tasks Models Count 
    openStatus = TaskStatusModel.objects.get(name = 'Open')
    open_task_count = TaskModel.objects.filter(Q(status = openStatus) & Q(property=property)).count()
     # maintenance count 
    maintenance_pending = MaintenanceStatusModel.objects.get(name = 'Pending')
    maintenance_count = MaintenanceRequest.objects.filter(Q(status = maintenance_pending) & Q(property=property)).count()

    context = {
        "property" : property,
        "properties_files" : properties_files,
        "open_task_count" : open_task_count,
        "maintenance_count" : maintenance_count
    }
    return render(request,'property/property_files.html',context)


# Property Maintenance Request 
def PropertyMaintenanceRequest(request,id):
    property = PropertyModel.objects.get(id = id)
    maintenance_requests = MaintenanceRequest.objects.filter(property = property).order_by('-date_created')
    # maintenance count 
    maintenance_pending = MaintenanceStatusModel.objects.get(name = 'Pending')
    maintenance_count = MaintenanceRequest.objects.filter(Q(status = maintenance_pending) & Q(property=property)).count()
    # Open Tasks Models Count 
    openStatus = TaskStatusModel.objects.get(name = 'Open')
    open_task_count = TaskModel.objects.filter(Q(status = openStatus) & Q(property=property)).count()

    # form data 
    properties = PropertyModel.objects.all()

    context = {
        "property" : property,
        "open_task_count" : open_task_count,
        "maintenance_requests" : maintenance_requests,
        "maintenance_count" : maintenance_count,
        "properties" : properties
    }

    return render(request,'property/property_request.html',context)


def PropertyFinancialsView(request,id):
    property = PropertyModel.objects.get(id = id)
    propertyExpenses = ExpenseModel.objects.filter(property =property)
    propertyIncome = IncomeModel.objects.filter(property =property)
    propertyRent = RentModel.objects.filter(property = property)

    # Totals Count 
    total_expense = propertyExpenses.aggregate(Sum('amount'))['amount__sum'] or 0
    property.total_expense = total_expense
    total_income = propertyIncome.aggregate(Sum('amount'))['amount__sum'] or 0
    property.total_income = total_income
    total_rent = propertyRent.aggregate(Sum('amount'))['amount__sum'] or 0
    property.total_rent = total_rent
    grand_total = (total_income + total_rent) - total_expense
    property.grand_total = grand_total


    # maintenance count 
    maintenance_pending = MaintenanceStatusModel.objects.get(name = 'Pending')
    maintenance_count = MaintenanceRequest.objects.filter(Q(status = maintenance_pending) & Q(property=property)).count()
    # Open Tasks Models Count 
    openStatus = TaskStatusModel.objects.get(name = 'Open')
    open_task_count = TaskModel.objects.filter(Q(status = openStatus) & Q(property=property)).count()

    context = {
        "property" : property,
        "propertyExpenses" : propertyExpenses,
        "propertyIncome" : propertyIncome,
        "propertyRent" : propertyRent,
        "total_expense" : total_expense,
        "total_income" : total_income,
        "total_rent" : total_rent,
        "grand_total" : grand_total,
        "open_task_count" : open_task_count,
        "maintenance_count" : maintenance_count,
    }


    return render(request,'property/financials_property_profile.html',context)
    

def PropertyShowings(request,id):
    property = PropertyModel.objects.get(id = id)
    # viewingsData = PropertyViewings.objects.filter(property = property)

    viewingsData = PropertyViewings.objects.filter(property=property).annotate(
    is_pending=Case(
        When(status='Pending', then=1),
        default=0,
        output_field=models.IntegerField(),
    )
    ).order_by('-is_pending', 'date_created')


    # maintenance count 
    maintenance_pending = MaintenanceStatusModel.objects.get(name = 'Pending')
    maintenance_count = MaintenanceRequest.objects.filter(Q(status = maintenance_pending) & Q(property=property)).count()
    # Open Tasks Models Count 
    openStatus = TaskStatusModel.objects.get(name = 'Open')
    open_task_count = TaskModel.objects.filter(Q(status = openStatus) & Q(property=property)).count()


    # Create Property Viewing
    if request.method == 'POST' and 'save_showing' in request.POST:
        save_viewing = PropertyViewings()
        save_viewing.viewing_date = request.POST.get('showingDate')
        save_viewing.viewing_time = request.POST.get('time')
        save_viewing.client = request.POST.get('viewingFor')
        save_viewing.contact = request.POST.get('contact')
        save_viewing.property = PropertyModel.objects.get(id=id)
        save_viewing.save()
        messages.success(request,'New Viewing Created') 
        return redirect('property-viewings', id)


    # Create Property Viewing
    if request.method == 'POST' and 'save_update' in request.POST:
        viewingID = request.POST.get('viewingID')
        save_edit = PropertyViewings.objects.get(id = viewingID)
        save_edit.viewing_time = request.POST.get('time')
        save_edit.client = request.POST.get('viewingFor')
        save_edit.contact = request.POST.get('contact')
        save_edit.status = request.POST.get('viewingStatus')
        viewing_date = request.POST.get('showingDate')
        if viewing_date:
            save_edit.viewing_date = viewing_date
        else:
            save_edit.viewing_date = save_edit.viewing_date
        save_edit.save()
        messages.success(request,'Viewing Updated') 
        return redirect('property-viewings', id)
    
    # Delete Viewing
    if request.method == 'POST' and 'delete_viewing' in request.POST:
        viewingID = request.POST.get('viewingID')
        delete_viewing = PropertyViewings.objects.get(id = viewingID)
        delete_viewing.delete()
        messages.success(request,'Successfully Deleted') 
        return redirect('property-viewings', id)


    context = {
        "property" : property,
        "open_task_count" : open_task_count,
        "maintenance_count" : maintenance_count,
        "viewingsData" : viewingsData
    }
    return render(request,'property/viewings.html',context)
    