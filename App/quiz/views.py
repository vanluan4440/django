from array import array
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import quiz

# Create your views here.
def create(request):
    question = request.POST['question']
    type = 'radio'
    point = int(request.POST['point'])
    Rightanswer = request.POST['an_correct']
    data = quiz.objects.create(question=question,type=type,answer=[request.POST['an1'],request.POST['an2'],request.POST['an3']],point=point,Rightanswer=Rightanswer)
    data.save()
    return JsonResponse({'id':data.id})

    
def edit(request):
    if not 'question' in request.POST:
        return HttpResponse('not found question')
    elif not 'type' in request.POST:
        return HttpResponse('not found type')
    elif not 'answer' in request.POST:
        return HttpResponse('not found answer')
    elif not 'point' in request.POST:
        return HttpResponse('not found point')
    elif not 'Rightanswer' in request.POST:
        return HttpResponse('not found right answer')
    elif not 'id' in request.POST:
        return HttpResponse('not found id')
    else:
        question = request.POST['question']
        type = request.POST['type']
        answer = request.POST['answer']
        point = int(request.POST['point'])
        Rightanswer = request.POST['Rightanswer']
        id = request.POST['id']
        quiz.objects.filter(id=id).update(question=question,type=type,answer=[answer],point=point,Rightanswer=Rightanswer)
        return HttpResponse('updated', status=200)
def delete(request,id):
    quiz.objects.filter(id=id).delete()
    return HttpResponse('deleted', status=200)
def getDetail(request):
    if not 'id' in request.POST:
        return HttpResponse('id not found', status='400')
    else:
        id = request.POST['id']
        data_lesson = quiz.objects.filter(id=id).values()
        return JsonResponse({"theQuiz": list(data_lesson)})
def getOnly(request,id):
    data = quiz.objects.filter(id=id).values()
    return JsonResponse({'quiz':list(data)})