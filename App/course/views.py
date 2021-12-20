from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.http import HttpResponse,JsonResponse
from .models import course
#title,desc ,img ,lesson ,create_on ,create_by 
# Create your views here.
def create(request):
    if request.method == 'POST':
        if not 'title' in request.POST:
            return HttpResponse('title not found', status=400)
        elif not 'img' in request.POST:
            return HttpResponse('image not found', status=400)
        elif not 'desc' in request.POST:
            return HttpResponse('desc not found', status=400)
        elif not 'lesson' in request.POST:
            return HttpResponse('lesson not found', status=400)
        elif not 'create_by' in request.POST:
            return HttpResponse('created_by not found', status=400)
        else:
            title = request.POST['title']
            img = request.POST['img']
            desc = request.POST['desc']
            lesson = request.POST['lesson']
            create_by = request.POST['create_by']
            now = datetime.now()
            course_data = course(title=title,desc= desc,img=img,lesson=[lesson], create_on = now, create_by = create_by)
            course_data.save()
            return HttpResponse('create course',status=200)
    else:
        return HttpResponse('none support', status=400)
def delete(request):
    session = request.session.get('user')
    if session == None:
        return HttpResponse('unauthorized', status=401)
    else:
        if not 'id' in request.POST:
            return HttpResponse('id not found',status=400)
        else:
            id = request.POST['id']
            course.objects.filter(id=id).delete()
            return HttpResponse('deleted', status=200)
def edit(request):
    if request.method == 'POST':
        if not 'title' in request.POST:
            return HttpResponse('title not found', status=400)
        elif not 'img' in request.POST:
            return HttpResponse('image not found', status=400)
        elif not 'desc' in request.POST:
            return HttpResponse('desc not found', status=400)
        elif not 'id' in request.POST:
            return HttpResponse('id not found', status=400)
        else:
            title = request.POST['title']
            img = request.POST['img']
            desc = request.POST['desc']
            id= request.POST['id']
            course.objects.filter(id=id).update(title=title,desc=desc,img=img)
            return HttpResponse('updated', status=200)
    else:
        return HttpResponse('no support', status=500)
def getAll(request):
    data_class = course.objects.all().values()
    return JsonResponse({"allCourse": list(data_class)})
def getOnly(request):
    if not 'id' in request.POST:
        return HttpResponse('id not found', status='400')
    else:
        id = request.POST['id']
        data_class = course.objects.filter(id=id).values()
        return JsonResponse({"theCourse": list(data_class)})