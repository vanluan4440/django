from django.urls import path
from . import views

urlpatterns = [
    path('create',views.create, name='create_lesson'),
    path('delete/<int:id>',views.delete, name='delete_lesson'),
    path('edit/<int:id>/<str:title>/<str:desc>',views.edit, name='edit_lesson'),
    path('getAll',views.getAll, name='getAll_lesson'),
    path('getOnly/<int:id>',views.getOnly, name='getOnly_lesson'),
    path('addQuiz/<int:idlesson>/<int:idquiz>',views.addQuizz, name='addQuizz'), 
    path('deleteQuiz/<int:idlesson>/<int:idquiz>',views.deleteQuiz, name='deleteQuizz'),  
    path('getRandom/<int:idlesson>/<int:amount>',views.getRandomQuiz, name='getRandomQuiz'),   
]