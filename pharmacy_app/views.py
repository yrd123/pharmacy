from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from .models import Pharmacist , Customer, Billing, Doctor, Medicine, Entry
# Create your views here.

def index(request):
    return redirect('login')


def signup(request):
    err=""
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        aadharNumber = request.POST.get('aadharNumber')
        if Pharmacist.objects.filter(email = email).exists():
            err = 'Email already taken. Try a different one.'
            print(err)
        elif Pharmacist.objects.filter(username = username).exists(): 
            err = "Username already Taken. Try a different one"
            print(err)
        elif Pharmacist.objects.filter(aadharNumber= aadharNumber).exists(): 
            err = "Aadhar number already Taken. Try a different one"
            print(err)
        else:
            obj1 = User.objects.create(
                username = username,
                email = email,
            )
            obj1.set_password(request.POST.get('password'))
            obj1.save()
            fullName = request.POST.get('fullName')  
            password = request.POST.get('password')
            contactNumber = request.POST.get('contactNumber')

            obj2 = Pharmacist.objects.create(
                email = email,
                username = username ,
                fullName = fullName,
                password = password,
                contactNumber = contactNumber,
                aadharNumber = aadharNumber 
                
            )
            obj2.save()
            return redirect("login")
        
    template_name = 'signup.html'
    context={'err':err}
    return render(request, template_name,context)




def login(request):
    err=""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
           err = 'Input correct email and password'
    template_name = 'login.html'
    context={'err':err}
    return render(request, template_name,context)

def logout(request):
    auth.logout(request)
    return redirect('/login')


def profile(request):
    pharmacist = Pharmacist.objects.get(username = request.user.username)
    return render(request, 'profile.html',{'pharmacist':pharmacist})


def schedule1(request):
    return render(request,'schedule1.html')

def schedule2(request):
    return render(request,'index.html')

def schedule3(request):
    return render(request,'index.html')

@login_required(login_url="login")
def dashboard(request):
    return render(request,'dashboard.html')

@login_required(login_url="login")
def registerCustomer(request):
    print("here")
    if request.method == 'POST':
        contactNumber = request.POST.get('contactNumber')
        email = request.POST.get('email')
        fullName = request.POST.get('fullName')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        aadharNumber = request.POST.get('aadharNumber')

        print(email)

        obj = Customer.objects.create(
            contactNumber =contactNumber ,
            email = email,
            fullName = fullName,
            address = address,
            dob=dob,
            aadharNumber = aadharNumber 
            
        )
        obj.save()

        return redirect('loginCustomer')


    return render(request,'registerCustomer.html')


@login_required(login_url="login")
def customer(request):
    err = ""
    if request.method == "POST":
        contactNumber = request.POST['contactNumber']
        if(Customer.objects.filter(contactNumber=contactNumber).exists()):
            customer = Customer.objects.get(contactNumber=contactNumber)
            bills = Billing.objects.filter(customer=customer)
            entries = Entry.objects.filter(bill__customer__contactNumber__contains = contactNumber)
            context = {"bills":bills, "customer":customer,'entries':entries}
            return render(request,'customer.html', context)
        else:
            err = "Enter a valid phone number"
    return render(request,'loginCustomer.html', {'err':err})



@login_required(login_url="login")
def loginCustomer(request):
    return render(request,'loginCustomer.html')

@login_required(login_url="login")
def billing(request):
    return render(request,'billing.html')
