from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
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
    

def edit(request):
    if request.method == 'POST':

        if not 'title' in request.POST:
            return HttpResponse('title not found', status=400)
        elif not 'img' in request.POST:
            return HttpResponse('image not found', status=400)
        elif not 'id' in request.POST:
            return HttpResponse('id not found', status=400)
        elif not 'desc' in request.POST:
            return HttpResponse('desc not found', status=400)
        else:
            title = request.POST['title']
            img = request.POST['img']
            desc = request.POST['desc']
            id= request.POST['id']
            now = date.today()
            dataClass = Class_A.objects.filter(id=id).update(title=title,img=img,desc=desc,created_on=now)
            return HttpResponse('updated', status=200)
    else:
        return HttpResponse('no support', status=500)

def getAll(request):
    data_class = Class_A.objects.all().values()
    return JsonResponse({"allClass": list(data_class)})

def getOnly(request):
    if not 'id' in request.POST:
        return HttpResponse('id not found', status='400')
    else:
        id = request.POST['id']
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
