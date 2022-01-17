from django.urls import path
from . import views

urlpatterns = [
    path('create',views.create, name='create_lesson'),
    path('delete',views.delete, name='delete_lesson'),
    path('edit',views.edit, name='edit_lesson'),
    path('getAll',views.getAll, name='getAll_lesson'),
    path('getOnly/<int:id>',views.getOnly, name='getOnly_lesson'),
   
]