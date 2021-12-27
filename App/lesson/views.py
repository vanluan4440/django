from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse,JsonResponse
from .models import lesson
# Create your views here.
def create(request):
    
    if not 'title' in request.POST:
        return HttpResponse('not found title')
    elif not 'img' in request.POST:
        return HttpResponse('not found image')
    elif not 'desc' in request.POST:
        return HttpResponse('not found desc')
    elif not 'file' in request.POST:
        return HttpResponse('not found file')
    elif not 'quiz' in request.POST:
        return HttpResponse('not found quiz')
    else:
        title = request.POST['title']
        img = request.POST['img']
        desc = request.POST['desc']
        file = request.POST['file']
        quiz = request.POST['quiz']
        create_on = datetime.now()
        data = lesson(title=title,img=img,desc=desc,file=file,quiz=[quiz], create_on= create_on)
        data.save()
        #print(data)
        return HttpResponse('created', status=200)
def delete(request):
    session = request.session.get('user')
    if session == None:
        return HttpResponse('unauthorized', status=401)
    else:
        if not 'id' in request.POST:
            return HttpResponse('id not found',status=400)
        else:
            id = request.POST['id']
            lesson.objects.filter(id=id).delete()
            return HttpResponse('deleted', status=200)
def edit(request):
    if request.method == 'POST':
        if not 'title' in request.POST:
            return HttpResponse('not found title')
        elif not 'img' in request.POST:
            return HttpResponse('not found image')
        elif not 'desc' in request.POST:
            return HttpResponse('not found desc')
        elif not 'file' in request.POST:
            return HttpResponse('not found file')
        elif not 'id' in request.POST:
            return HttpResponse('id not found', status=400)
        else:
            title = request.POST['title']
            img = request.POST['img']
            desc = request.POST['desc']
            file = request.POST['file']
            id= request.POST['id']
            lesson.objects.filter(id=id).update(title=title,desc=desc,img=img, file= file)
            return HttpResponse('updated', status=200)
def getAll(request):
    data_lesson = lesson.objects.all().values()
    return JsonResponse({"allLesson": list(data_lesson)})
def getOnly(request):
    if not 'id' in request.POST:
        return HttpResponse('id not found', status='400')
    else:
        id = request.POST['id']
        data_lesson = lesson.objects.filter(id=id).values()
        return JsonResponse({"theLesson": list(data_lesson)})
