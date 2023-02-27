from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile


def login_user(request : HttpRequest):
    msg = "Error Loging, Try Again..."
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('main:home_page')
        else:
            
            return render(request,'account/login.html' ,{"msg" : msg})

    return render(request, 'account/login.html' )



def logout_user(request: HttpRequest):
    logout(request)
    return redirect('account:login')


def register_user(request : HttpRequest):

    if request.method == "POST":
        new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"])
        new_user.save()


        #if register successful redirect to sign in page
        return redirect("account:login")
    return render(request, "account/register.html")