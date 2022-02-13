from django.urls import path
from . import views

urlpatterns = [
    path('create',views.create, name='create_quiz'),
    path('delete/<int:id>',views.delete, name='delete_quiz'),
    path('edit',views.edit, name='edit_quiz'),
    path('getDetail',views.getDetail, name='getDetail_quiz'),
     path('getOnly/<int:id>',views.getOnly, name='getOnly'),
   
]