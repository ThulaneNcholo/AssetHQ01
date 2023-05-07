from django.shortcuts import render
from django.db.models import Sum

# Other models import 
from Requests.models import *
from Tasks.models import *
from applications.models import *
from property.models import *
from Financials.models import *

# Create your views here.
def IndexView(request):
    # property select data 
    properties = PropertyModel.objects.all()
    
    # Property Viewings data 
    propertyShowingsCount = PropertyViewings.objects.filter(status = 'Pending').count()
     
    if propertyShowingsCount <= 3:
        propertyShowings = PropertyViewings.objects.filter(status = 'Pending')[:3]
        view_more = 'False'
    else:
        propertyShowings = PropertyViewings.objects.filter(status = 'Pending')[:3]
        view_more = 'True'
    
    # maintenance data 
    maintenance_Pending = MaintenanceStatusModel.objects.get(name = 'Pending')
    maintenance_request = MaintenanceRequest.objects.filter(status = maintenance_Pending)

    # tasks data 
    task_status = TaskStatusModel.objects.get(name = 'Open')
    open_task = TaskModel.objects.filter(status = task_status)

    # Application data 
    applications =  ApplicationModel.objects.all()

    # property viewings 
    properties_viewings = PropertyModel.objects.all()

    # Financials 
    Expenses = ExpenseModel.objects.all()
    total_expense = Expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    All_Expenses = total_expense

    rent_roll = RentModel.objects.all()
    total_rent_roll = rent_roll.aggregate(Sum('amount'))['amount__sum'] or 0

    income = IncomeModel.objects.all()
    total_incomes = income.aggregate(Sum('amount'))['amount__sum'] or 0

    Total_Income = (total_rent_roll + total_incomes) - All_Expenses

    context = {
        "maintenance_request" : maintenance_request,
        "open_task" : open_task,
        "applications" : applications,
        "properties_viewings": properties_viewings,
        "All_Expenses" : All_Expenses,
        "Total_Income" : Total_Income,
        "propertyShowings" : propertyShowings,
        "properties" : properties,
        "view_more" : view_more
    }
    return render(request,'client/index.html',context)

def Users(request):
    return render(request,'client/users.html')
