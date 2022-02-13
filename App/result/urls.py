from django.urls import path
from . import views


urlpatterns = [
    path('create',views.create, name='createResult'),
    path('getResultByUser',views.getResultByUser, name='getResultByUser'),
    path('getResultByLesson',views.getResultByLesson, name='getResultByLesson'),
   
]