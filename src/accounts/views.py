from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                return HttpResponse('username is taken')
            else:
                if User.objects.filter(email=email).exists():
                    return HttpResponse('email is being used')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    return redirect('login')
        else:
            return HttpResponse('Invalid password')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponse('You are now logged in')
        else:
            return HttpResponse('Invalid credentials ')
    else:
        return render(request, 'login.html')
