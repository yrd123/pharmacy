from django.shortcuts import render, redirect
# Create your views here.

def index(request):
    return render(request,'index.html')


def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def schedule1(request):
    return render(request,'schedule1.html')

def schedule2(request):
    return render(request,'index.html')

def schedule3(request):
    return render(request,'index.html')

def registerCustomer(request):
    return render(request,'registerCustomer.html')

def loginCustomer(request):
    return render(request,'loginCustomer.html')

def customer(request):
    return render(request,'customer.html')


def billing(request):
    return render(request,'billing.html')
