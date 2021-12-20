from django.urls import path
from . import views

urlpatterns = [
    path('create',views.create, name='create_class'),
    path('delete',views.delete, name='delete_class'),
    path('edit',views.edit, name='edit_class'),
    path('getAll',views.getAll, name='getAll_class'),
    path('getOnly',views.getOnly, name='getOnly_class'),
   
]