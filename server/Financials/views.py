from django.shortcuts import render,redirect
from django.contrib import messages 
from .models import ExpenseModel,IncomeModel,RentModel
# other models 
from property.models import PropertyModel
from applications.models import ApplicationModel

from django.db.models import Sum

# Create your views here.
def ListFinancials(request):
    properties = PropertyModel.objects.all()
    all_expenses = ExpenseModel.objects.all()
    all_total_expenses = all_expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    all_income = IncomeModel.objects.all()
    all_total_income = all_income.aggregate(Sum('amount'))['amount__sum'] or 0
    all_rent = RentModel.objects.all()
    all_total_rent = all_rent.aggregate(Sum('amount'))['amount__sum'] or 0
    grand_total = (all_total_income + all_total_rent) - all_total_expenses

    for property in properties:
        # expenses 
        expenses = ExpenseModel.objects.filter(property=property)
        total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
        property.total_expense = total_expense
        # income 
        income = IncomeModel.objects.filter(property=property)
        total_income = income.aggregate(Sum('amount'))['amount__sum'] or 0
        property.total_income = total_income
        # Rent Collection 
        rent = RentModel.objects.filter(property=property)
        total_rent = rent.aggregate(Sum('amount'))['amount__sum'] or 0
        property.total_rent = total_rent
        # Net total 
        total_net = (total_income + total_rent) - total_expense
        property.total_net = total_net


    context = {
        "properties" : properties,
        "all_total_expenses" : all_total_expenses,
        "all_total_income" : all_total_income,
        "all_total_rent" : all_total_rent,
        "grand_total" : grand_total
        }

    return render(request,'Financials/list_financials.html',context)

# View Property Financials 
def PropertyFinancials(request,id):
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

    context = {
        "propertyExpenses" : propertyExpenses,
        "propertyIncome" : propertyIncome,
        "propertyRent" : propertyRent,
        "total_expense" : total_expense,
        "total_income" : total_income,
        "total_rent" : total_rent,
        "grand_total" : grand_total
    }
    return render(request,'Financials/property_financials.html',context)


# Forms start 
def ExpensesForm(request,id):

    if request.method == 'POST' and 'submit_expense' in request.POST:
        save_expense = ExpenseModel()
        save_expense.name = request.POST.get('name')
        save_expense.description = request.POST.get('description')
        save_expense.amount = request.POST.get('amount')
        save_expense.property = PropertyModel.objects.get(id =id )
        save_expense.save()
        return redirect('property-financials', id)

    return render(request,'Financials/expenseForm.html')

def IncomeForm(request,id):

    if request.method == 'POST' and 'submit_income' in request.POST:
        save_income = IncomeModel()
        save_income.name = request.POST.get('name')
        save_income.description = request.POST.get('description')
        save_income.amount = request.POST.get('amount')
        save_income.property = PropertyModel.objects.get(id =id )
        save_income.save()
        return redirect('property-financials', id )
    
    return render(request,'Financials/incomeForm.html')

def RentForm(request,id):
    property = PropertyModel.objects.get(id = id)
    propertyTenants = property.tenants.all()
    TenantID = request.session.get('tenant_id')

    if request.method == 'POST' and 'submit_rent' in request.POST:
        save_rent = RentModel()
        save_rent.property = property
        save_rent.name = request.POST.get('name')
        save_rent.amount = request.POST.get('amount')
        save_rent.tenant = ApplicationModel.objects.get(id = TenantID)
        save_rent.save()
        return redirect('property-financials', id )

    context = {
        "propertyTenants" : propertyTenants
    }
    return render(request,'Financials/rentForm.html',context)

def RentTenantPartial(request):

    if request.method == 'POST':
        financial_applicant = request.POST.get('financial_applicant')
        request.session['tenant_id'] = financial_applicant
        tenant_profile = ApplicationModel.objects.get(id = financial_applicant)

        context = {
            "tenant_profile" : tenant_profile
        }

    
    return render(request,'partials/rent_tenant_partial.html',context)
