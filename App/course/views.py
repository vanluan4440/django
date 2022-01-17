from django.shortcuts import render
from datetime import date
import os
# Create your views here.
from django.http import HttpResponse,JsonResponse


from .models import course

import random
import jwt

#title,desc ,img ,lesson ,create_on ,create_by 
# Create your views here.
def handle_uploaded_file(f):
    name = random.randrange(1,10000000000)
    url  = 'static/{}.png'.format(name)
    with open(url, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return '{}.png'.format(name)
def create(request):
    if request.method == 'POST':
        token = request.COOKIES.get('token')
        if not token:
            return HttpResponse('unauthentication', status = 400)
        try:
            payload = jwt.decode(token,'secret',algorithms='HS256')
        except jwt.ExpiredSignatureError:
            return HttpResponse('unauthentication', status = 400)
        image = handle_uploaded_file(request.FILES.get('img'))
        title = request.POST.get('title')
        desc = request.POST.get('desc')    
        course_data = course.objects.create(title=title,desc= desc,img=image,lesson=[], create_on = date.today(), create_by = payload['id'])
        course_data.save()
        idcourse = course_data.id
        return JsonResponse({'idCourse':idcourse})
    else:
        return HttpResponse('none support', status=400)
def delete(request,id):
    data_course = course.objects.filter(id=id)
    url  = 'static/{}'.format(list(data_course.values())[0]['img'])
    os.remove("{}".format(url))
    data_course.delete()
    return HttpResponse('deleted', status=200)
def edit(request,id,title,desc):
   
       
    course.objects.filter(id=id).update(title=title,desc=desc)
    return HttpResponse('updated', status=200)
  
def getAll(request):
    data_class = course.objects.all().values()
    return JsonResponse({"allCourse": list(data_class)})
def getOnly(request,id):
    data_course = list(course.objects.filter(id=id).values())[0]
    return JsonResponse(data_course)
def addLesson(request, idcourse, idlesson):
    data = list(course.objects.filter(id=idcourse).values())[0]['lesson']
    data.append({'idlesson': idlesson})
    course.objects.filter(id=idcourse).update(lesson =data )
    return HttpResponse(status=200)
