from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import quiz

# Create your views here.
def create(request):
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
    else:
        question = request.POST['question']
        type = request.POST['type']
        answer = request.POST['answer']
        point = int(request.POST['point'])
        Rightanswer = request.POST['Rightanswer']
        data = quiz(question=question,type=type,answer=[answer],point=point,Rightanswer=Rightanswer)
        data.save()
        return HttpResponse('created')

    
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