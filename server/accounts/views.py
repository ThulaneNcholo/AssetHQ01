from django.shortcuts import render,redirect
from .models import UserModel
from django.contrib import messages




# Authentication Imports start 
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_user
from django.contrib.auth.models import Group
# Authentication Imports end 



# Authentication Views start
# login User 
@unauthenticated_user
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')
            
    return render(request, "Authentication/login.html")


# Agent Register view start 
@unauthenticated_user
def RegisterUser(request):
    form = CreateUserForm()
    if request.method == 'POST' and 'create-customer' in request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            cleitnemail = form.cleaned_data.get('email')
            UserModel.objects.create(
                user= user,
                first_name=username,
                email = cleitnemail
            )
            messages.success(request,'Account was created for ' + username)
            return redirect("login")

    context = {
        'form' : form
    }
    return render(request, "Authentication/customer_register.html", context)


# logout user 
def LogoutUser(request):
    logout(request)
    return redirect('login')

# Authentication Views End 