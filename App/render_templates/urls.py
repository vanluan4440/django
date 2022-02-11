from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # index login
    path('login',views.login, name='login'),
    # sign up
    path('signup',views.signup, name='signup'),
    #instructor dashboard
    path('instructor/dashboard',views.InstructorDashboard, name='InstructorDashboard'),
    #instructor profile
    path('instructor/profile',views.InstructorProfile, name='InstructorProfile'),
    #edit account
    path('instructor/edit/account/<int:id>',views.InstructorEditAccount, name='InstructorEditAccount'),

    #create class
    path('instructor/detail',views.DetailClass, name='DetailClass'),

    #create course
    path('instructor/course',views.DatailCourse, name='DatailCourse'),

    #create quizz
    path('instructor/lesson',views.DatailLesson, name='DatailLesson'),
    
   
]

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)