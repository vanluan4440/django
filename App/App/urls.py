"""App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    #login register logout user
    path('api/', include('api.urls')),
    # create edit delete class
    path('class/', include('class.urls')),
    # create edit delete course
    path('course/', include('course.urls')),
    # create edit delete lesson
    path('lesson/', include('lesson.urls')),

    #quiz
    path('quiz/', include('quiz.urls')),
    #render_templates
    path('', include('render_templates.urls')),
    #result
    path('result/', include('result.urls')),
    #exam
    path('exam/', include('exam.urls')),

    # result course
    path('resultCourse/', include('resultCourse.urls')),


]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
