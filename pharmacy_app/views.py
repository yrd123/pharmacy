from django.shortcuts import render, redirect
# Create your views here.

def index(request):
    return render(request,'index.html')


def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def schedule1(request):
    return render(request,'index.html')

def schedule2(request):
    return render(request,'index.html')

def schedule3(request):
    return render(request,'index.html')
