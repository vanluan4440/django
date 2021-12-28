from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import jwt
from api.models import User 



# Create your views here.
def login(request):
    from django.middleware.csrf import get_token
    get_token(request)
    return render(request, template_name='login/login.html')
def signup(request):
    from django.middleware.csrf import get_token
    get_token(request)
    return render(request,template_name='login/signup.html')
#instructor dashboard
def InstructorDashboard(request):
    from django.middleware.csrf import get_token
    get_token(request)
    token = request.COOKIES.get('token')
    
    if not token:
        return redirect('/login')
    try:
        payload = jwt.decode(token,'secret',algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return redirect('/login')
    user = User.objects.filter(id =payload['id'] ).count()
    if user <1:
        return redirect('/login')
    else:
        return render(request,template_name='instructor/dashboard.html')
def InstructorProfile(request):
    from django.middleware.csrf import get_token
    get_token(request)
    token = request.COOKIES.get('token')
    
    if not token:
        return redirect('/login')
    try:
        payload = jwt.decode(token,'secret',algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return redirect('/login')
    user = User.objects.filter(id =payload['id'] ).count()
    if user <1:
        return redirect('/login')
    else:
        return render(request,template_name='instructor/profile.html')
    
def InstructorEditAccount(request,id):
    from django.middleware.csrf import get_token
    get_token(request)
    token = request.COOKIES.get('token')
    
    if not token:
        return redirect('/login')
    try:
        payload = jwt.decode(token,'secret',algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return redirect('/login')
    user = User.objects.filter(id =payload['id'] ).count()
    if user <1:
        return redirect('/login')
    else:
        return render(request,template_name='instructor/account-edit.html')
    
  



