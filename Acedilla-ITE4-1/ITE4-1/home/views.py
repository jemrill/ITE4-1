from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from home.models import Contact
from django.contrib.auth.forms import UserCreationForm
from home.forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from .models import  Destination

@login_required(login_url='login')
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method=="POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')
                
        context = {'form':form}
        return render(request, 'register.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("/")

            else:  
                
                messages.info(request, 'Username OR password is incorrect')
                return render(request,'login.html')
            

        return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")


def blog(request):

    dests = Destination.objects.all()

    return render(request,"blog.html", {'dests' : dests})

@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        father = request.POST.get('father')
        mother = request.POST.get('mother')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        phone1 = request.POST.get('phone1') 
        Address1 = request.POST.get('Address1')
        Address2 = request.POST.get('Address2')     
        file = request.FILES["file"]
        file1 = request.FILES["file1"]

        document = Contact.objects.create(name=name,father=father,mother=mother,
        email=email, phone=phone, phone1=phone1,  Address1=Address1, Address2=Address2, 
        file=file,file1=file1)
        document.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, "contact.html")