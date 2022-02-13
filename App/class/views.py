from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse

from course.models import course


# Connect to the database
from .models import Class_A
import os
# Create your views here.
from datetime import date
today = date.today()
import random
import json
import jwt
def handle_uploaded_file(f):
    name = random.randrange(1,10000000000)
    url  = 'static/{}.png'.format(name)
    with open(url, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return '{}.png'.format(name)

#create class
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
        id = payload['id']
        course = []
        now = date.today()
        dataClass = Class_A(title = title, img= image, desc= desc,created_on=now,course=course,createdBy=id)
        dataClass.save()
        return HttpResponse('created', status=200)
    else:
        return HttpResponse('no support', status=500)

def delete(request,id):
    token = request.COOKIES.get('token')
    if not token:
        return HttpResponse('unauthentication', status = 400)
    try:
        payload = jwt.decode(token,'secret',algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return HttpResponse('unauthentication', status = 400)
   
    data_class = Class_A.objects.filter(id=id)
    url  = 'static/{}'.format(list(data_class.values())[0]['img'])
    os.remove("{}".format(url))
    data_class.delete()
    return HttpResponse('deleted', status=200)
    

def edit(request,id,title,desc):
    if request.method == 'POST':
        dataClass = Class_A.objects.filter(id=id).update(title=title,desc=desc)
        return HttpResponse('updated', status=200)
    else:
        return HttpResponse('no support', status=500)

def getAll(request):
    data_class = Class_A.objects.all().values()
    return JsonResponse({"allClass": list(data_class)})

def getOnly(request,id):
    data_class = Class_A.objects.filter(id=id).values()
    return JsonResponse({"theClass": list(data_class)})
def getClassByUser(request):
    token = request.COOKIES.get('token')
    if not token:
        return HttpResponse('unauthentication', status = 400)
    try:
        payload = jwt.decode(token,'secret',algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return HttpResponse('unauthentication', status = 400)
    data = Class_A.objects.filter(createdBy= payload['id']).values()
    return JsonResponse({'ClassByUser': list(data)})
def addCourse(request,idclass,idcourse):
    course_a = list(Class_A.objects.filter(id=idclass).values())[0]['course']
    course_a.append({'idcourse': idcourse})
    Class_A.objects.filter(id=idclass).update(course =course_a )
    return HttpResponse(status=200)
def deleteCourse(resquest,idclass,idcourse):
    course_a = list(Class_A.objects.filter(id=idclass).values())[0]['course']
    new_array = []
    for i in course_a:
        if i['idcourse'] != idcourse:
            new_array.append(i)
    Class_A.objects.filter(id=idclass).update(course=new_array)
    return HttpResponse('delete')
