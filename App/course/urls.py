from django.urls import path
from . import views

urlpatterns = [
    path('create',views.create, name='create_course'),
    path('delete',views.delete, name='delete_course'),
    path('edit',views.edit, name='edit_course'),
    path('getAll',views.getAll, name='getAll_course'),
    path('getOnly',views.getOnly, name='getOnly_course'),
   
]