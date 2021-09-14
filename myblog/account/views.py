from django.shortcuts import render,redirect

from blogPost import urls
from blogPost.urls import *

from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account is created for '+user)
            return redirect('login')


    context={'form':form}

    return render(request,'user_account/register.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect!')
            return render(request, 'user_account/login.html')

    return render(request, 'user_account/login.html')

def logoutUser(request):
    logout(request)
    return redirect('home') 




