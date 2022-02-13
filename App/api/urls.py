from django.urls import path
from . import views


urlpatterns = [
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('logout',views.logout, name='logout'),
    path('getUser',views.getUser, name='getUser'),
    #path('token',views.token, name='token'),
    #getUserDatail
    path('getUserDatail',views.getUserDatail, name='getUserDatail'),
   
]