
import json
from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.http import HttpResponse,JsonResponse, response
# Connect to the database
from .models import User
import jwt
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
            payload = {
                'id' : check.values()[0]['id'],
                'email':email,
                'author': check.values()[0]['author']
            }
            token = jwt.encode(payload,"secret", algorithm="HS256")
            response = HttpResponse( token )
            response.set_cookie('token', token)
            return JsonResponse({'status':200,'mess':'Login successfully','author': check.values()[0]['author'] ,'token': token})
        else:
            return JsonResponse({'mess':"email or password wrong",'status':400})


#register

def register(request):
    from django.middleware.csrf import get_token
    get_token(request)
    username= request.POST["username"]
    password = request.POST["password"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    author = False
    if request.POST["author"] == 'true':
        author = True
    now = datetime.now()
    if User.objects.filter(email=email).count()>0:
        return JsonResponse({'mess':"Account Is Ready"})
    else:
        user = User(username=username,password=password,email=email,phone=phone,author=author,created_on=now)
        user.save()
        return JsonResponse({'mess': "Signup successfully"})
def token(request):
    from django.middleware.csrf import get_token
    get_token(request)  #This causes django to set the csrftoken cookie in the response

    return HttpResponse('server received GET request')
def logout(request):
    from django.middleware.csrf import get_token
    get_token(request)
    try:
        del request.session['user']
        del request.session['id']
        return HttpResponse('LoggedOut',status=200)
    except:
        return HttpResponse('LoggedOut',status=200)
def getUser(request):
    token = request.COOKIES.get('token')
    payload = jwt.decode(token,'secret',algorithms='HS256')
    user = list(User.objects.filter(id=payload['id']).values())[0]
    data = {
        'username': user['username'],
        'email': user['email'],
        'phone': user['phone'],
        'author': user['author']
    }
    return JsonResponse(data)