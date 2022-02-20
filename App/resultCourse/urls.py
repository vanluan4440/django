from django.urls import path
from . import views


urlpatterns = [
    path('create',views.create, name='createResultCourse'),
    path('getResultByCourse',views.getResultByCourse, name='getResultByCourse'),
    path('getResultByUser',views.getResultByUser, name='getResultByUser'),
   
]