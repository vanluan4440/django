from django.urls import path
from . import views

urlpatterns = [
    path('create',views.create, name='create_course'),
    path('delete/<int:id>',views.delete, name='delete_course'),
    path('edit/<int:id>/<str:title>/<str:desc>',views.edit, name='edit_course'),
    path('getAll',views.getAll, name='getAll_course'),
    path('getOnly/<int:id>',views.getOnly, name='getOnly_course'),
    path('addLesson/<int:idcourse>/<int:idlesson>',views.addLesson, name='addLesson'),
]