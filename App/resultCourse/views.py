
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import resultCourse
from datetime import date
import jwt
def create(request):
    if request.method == 'POST':
        token = request.COOKIES.get('token')
        courseid = request.POST['course']
        point = request.POST['point']
        if not token:
            return HttpResponse('unauthentication', status = 400)
        try:
            payload = jwt.decode(token,'secret',algorithms='HS256')
        except jwt.ExpiredSignatureError:
            return HttpResponse('unauthentication', status = 400)
        data = resultCourse.objects.create(userid=payload['id'],courseid=courseid, point=point,date=date.today())
        data.save()
        return JsonResponse({'mess':'success'})
    else:
        return HttpResponse('none support', status=400)
def getResultByCourse(request):
    token = request.COOKIES.get('token')
    courseid = request.POST['courseid']
    if not token:
        return HttpResponse('unauthentication', status = 400)
    try:
        payload = jwt.decode(token,'secret',algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return HttpResponse('unauthentication', status = 400)
        
    data = resultCourse.objects.filter(courseid=courseid).values()
    return JsonResponse({'history':list(data)})
def getResultByUser(request):
    token = request.COOKIES.get('token')
    if not token:
        return HttpResponse('unauthentication', status = 400)
    try:
        payload = jwt.decode(token,'secret',algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return HttpResponse('unauthentication', status = 400)
        
    data = resultCourse.objects.filter(userid=payload['id']).values()
    return JsonResponse({'history':list(data)})