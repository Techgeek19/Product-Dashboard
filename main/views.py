from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import loginform,registerform
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        form= registerform(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            first_name= form.cleaned_data.get('first_name')
            last_name= form.cleaned_data.get('last_name')
            email= form.cleaned_data.get('email')
            password= form.cleaned_data.get('password')
            cpassword = form.cleaned_data.get("confirm_password")
            user = User.objects.create_user(username=username, first_name= first_name, last_name =last_name, email=email, password=password)
            user.save(); 
            messages.success(request,'Registered successfully..Login here')
            return redirect('login')
    else:
        return render (request, 'register.html', {'form': registerform})

def login(request):
    if request.method=='POST':
        form=loginform(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            try:
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect ('plist')
                else: 
                    messages.warning(request,'Invalid Credentials')

            except ObjectDoesNotExist:
                print("invalid user") 
    return render (request,'login.html', context={'form': loginform})

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def plist(request):
    obj= product.objects.all()
    return render(request,'plist.html', {'obj': obj})

@login_required(login_url='/login/')
def pdetail(request):
    obj= product.objects.all()
    return render(request,'pdetail.html', {'obj': obj})
