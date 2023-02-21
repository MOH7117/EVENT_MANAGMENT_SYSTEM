from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.contrib import messages


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