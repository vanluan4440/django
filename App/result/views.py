
from telnetlib import STATUS
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import result
from datetime import date
import jwt
def create(request):
    if request.method == 'POST':
        token = request.COOKIES.get('token')
        lessonid = request.POST['lesson']
        point = request.POST['point']
        if not token:
            return HttpResponse('unauthentication', status = 400)
        try:
            payload = jwt.decode(token,'secret',algorithms='HS256')
        except jwt.ExpiredSignatureError:
            return HttpResponse('unauthentication', status = 400)
        
        data = result.objects.create(userid=payload['id'],lessonid=lessonid, point=point,date=date.today())
        data.save()
        return JsonResponse({'mess':'success'})
    else:
        return HttpResponse('none support', status=400)
def getResultByUser(request):
    token = request.COOKIES.get('token')
    if not token:
        return HttpResponse('unauthentication', status = 400)
    try:
        payload = jwt.decode(token,'secret',algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return HttpResponse('unauthentication', status = 400)
        
    data = result.objects.filter(userid=payload['id']).values()
    return JsonResponse({'history':list(data)})
def getResultByLesson(request):
    token = request.COOKIES.get('token')
    lessonid = request.POST['lessonid']
    if not token:
        return HttpResponse('unauthentication', status = 400)
    try:
        payload = jwt.decode(token,'secret',algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return HttpResponse('unauthentication', status = 400)
        
    data = result.objects.filter(lessonid=lessonid).values()
    return JsonResponse({'history':list(data)})
    