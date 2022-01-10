from django.urls import path
from . import views

urlpatterns = [
    # index login
    path('login',views.login, name='login'),
    # sign up
    path('signup',views.signup, name='signup'),
    #instructor dashboard
    path('instructor/dashboard',views.InstructorDashboard, name='InstructorDashboard'),
    #instructor profile
    path('instructor/profile',views.InstructorProfile, name='InstructorProfile'),
    #edit account
    path('instructor/edit/account/<int:id>',views.InstructorEditAccount, name='InstructorEditAccount'),

    #create class
    path('instructor/create-class',views.CreateClass, name='CreateClass'),
    
   
]