
from urllib import request
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse,JsonResponse
from .models import Exam
import random
import jwt
from datetime import date
import json
# Create your views here.
def create(request):
    token = request.COOKIES.get('token')
    if not token:
        return HttpResponse('unauthentication', status = 400)
    try:
        payload = jwt.decode(token,'secret',algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return HttpResponse('unauthentication', status = 400)
    dateStart= request.POST['start']
    dateEnd = request.POST['end']
    time = request.POST['time']
    listquestion = request.POST['list']
    course = request.POST['course']
   
    data = Exam.objects.create(nameExam='Exam',DateStart=dateStart,EndDate=dateEnd, Time= time,ListQuestion=listquestion,createBy=payload['id'],course=course )
    data.save()
    return HttpResponse('success', status=200)
def getAllExam(request):
    id = request.POST['id']
    data = Exam.objects.filter(course=id).values()
    return JsonResponse({'data':list(data)})
def getOnlyExam(request):
    id = request.POST['id']
    data= Exam.objects.filter(id=id).values()
    return JsonResponse({'data':list(data)})