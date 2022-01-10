from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.http import HttpResponse,JsonResponse
# Connect to the database
from .models import Class_A
# Create your views here.
import json

#create class
def create(request):
    if request.method == 'POST':
        print(request.FILES.get('img'))
        print(request.POST.get('title'))
       
        return HttpResponse('created')
        # if not 'title' in request.POST:
        #     return HttpResponse('title not found', status=400)
        # elif not 'img' in request.POST:
        #     return HttpResponse('image not found', status=400)
        # elif not 'desc' in request.POST:
        #     return HttpResponse('desc not found', status=400)
        
        # else:
        #     title = request.POST['title']
        #     img = request.POST['img']
        #     desc = request.POST['desc']
        #     course = []
        #     now = datetime.now()
        #     dataClass = Class_A(title = title, img= img, desc= desc,created_on=now,course=course,createdBy=18)
        #     print(dataClass)
        #     dataClass.save()
        #     return HttpResponse('created', status=200)
    else:
        return HttpResponse('no support', status=500)

def delete(request):
    session = request.session.get('user')
    if session == None:
        return HttpResponse('unauthorized', status=401)
    else:
        if not 'id' in request.POST:
            return HttpResponse('id not found',status=400)
        else:
            id = request.POST['id']
            data_class = Class_A.objects.filter(id=id).delete()
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
            now = datetime.now()
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