from django.urls import path
from . import views

urlpatterns = [
    path('add',views.create, name='create'),
    path('getAll',views.getAllExam, name='getAllExam'),
    path('getOnly',views.getOnlyExam, name='getOnlyExam'),
    
]