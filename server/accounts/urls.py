from . import views
from django.urls import path

urlpatterns = [
    # Authentication urls start 
    path('login/', views.LoginPage,name="login"),
    path('register/', views.RegisterUser,name="register"),
    path('logout/', views.LogoutUser,name="logout"),
    # Authentication urls end 
]