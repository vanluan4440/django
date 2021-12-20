
import json
from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.http import HttpResponse,JsonResponse
# Connect to the database
from .models import User
#login
def login(request):
    from django.middleware.csrf import get_token
    get_token(request) 
    if request.method == 'GET':
        return HttpResponse('get')
    elif request.method == 'POST':
        password = request.POST["password"]
        email = request.POST["email"]
        check = User.objects.filter(email=email,password=password)
        if(check):
            request.session['user'] = email
            return HttpResponse({'mess: Logined'}, status=200)
        else:
            return HttpResponse("email or password wrong",status=400)


#register

def register(request):
    from django.middleware.csrf import get_token
    get_token(request)
    username= request.POST["username"]
    password = request.POST["password"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    author = request.POST["author"]
    now = datetime.now()
    if User.objects.filter(email=email).count()>0:
        return JsonResponse({'mess':"AccountIsReady"})
    else:
        user = User(username=username,password=password,email=email,phone=phone,author=author,created_on=now)
        user.save()
        return JsonResponse({'mess': "Registed"})
def token(request):
    from django.middleware.csrf import get_token
    get_token(request)  #This causes django to set the csrftoken cookie in the response

    return HttpResponse('server received GET request')
def logout(request):
    from django.middleware.csrf import get_token
    get_token(request)
    try:
        del request.session['user']
        return HttpResponse('LoggedOut',status=200)
    except:
        return HttpResponse('LoggedOut',status=200)
   