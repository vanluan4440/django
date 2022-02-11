from msilib.schema import File
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse,JsonResponse
from .models import lesson
import random
import jwt
from datetime import date
# Create your views here.
def handle_uploaded_file(f):
    name = random.randrange(1,10000000000)
    url  = 'static/{}.png'.format(name)
    with open(url, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return '{}.png'.format(name)
def handle_uploaded_file_doc(f):
    name = random.randrange(1,10000000000)
    url  = 'static/{}.doc'.format(name)
    with open(url, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return '{}.doc'.format(name)
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
        file = handle_uploaded_file_doc(request.FILES.get('doc'))
        title = request.POST.get('title')
        desc = request.POST.get('desc')    
        data = lesson.objects.create(title=title,desc= desc,img=image,file=file,quiz=[], create_on = date.today(), create_by = payload['id'])
        data.save()
        idLesson = data.id
        return JsonResponse({'idLesson':idLesson})
    else:
        return HttpResponse('none support', status=400)
def delete(request,id):
    lesson.objects.filter(id=id).delete()
    return HttpResponse('deleted', status=200)
def edit(request,id,title,desc):
        lesson.objects.filter(id=id).update(title=title,desc=desc)
        return HttpResponse('updated', status=200)
def getAll(request):
    data_lesson = lesson.objects.all().values()
    return JsonResponse({"allLesson": list(data_lesson)})
def getOnly(request,id): 
    data_lesson = list(lesson.objects.filter(id=id).values())[0]
    return JsonResponse(data_lesson)
def addQuizz(request,idlesson,idquiz):
    data = list(lesson.objects.filter(id=idlesson).values())[0]['quiz']
    data.append({'idQuiz': idquiz})
    lesson.objects.filter(id=int(idlesson)).update(quiz=data )
    print(data)
    return HttpResponse(status=200)


