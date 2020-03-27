from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=name).exists():
                messages.info(request,'username is already taken.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists.')
                return redirect('register')
            else:
                user=User.objects.create_user(username=name,email=email,password=password)
                user.save()
                print("user saved")
              
        else:
            messages.info(request,'password not matching...')
            return redirect('register')
        return redirect('login')
    else:
        return render(request,"register.html")

def police(request):
    return render(request,"police.html")
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("user login done")
            return redirect('/afterlogincompany')
        else:
            messages.info(request,'invalid credentials')
            print("gone")
            return redirect('login')
    else:
        return render(request,"login.html")  

def client(request):
    return render(request,"client.html")

def developer(request):
    return render(request,"developer.html")

def company(request):
    return render(request,"company.html")  

def afterreg(request):
    return render(request,"afterreg.html")

def afterlogincompany(request):
    return render(request,"afterlogincompany.html")