import sys
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from exam_interview.models import *
from exam_interview.forms import *

# Create your views here.

def cover(request):
    if not request.user.is_authenticated:
        return render(request,'cover.html')
    else:
        return redirect('home')
        

def loginview(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.warning(request,'Invalid Credentials')
                return redirect('login')
        return render(request,'login.html')
    else:
        return redirect('home')


def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request,'logout.html')
    else:
        return redirect('lr')


def registerview(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            # Checking Already Data Has Been Recorded or Not..!

            # Username
            if User.objects.filter(username = request.POST['username']):
                messages.warning(request,'Username already exists')
                return render(request,'register.html')

            # Email
            elif User.objects.filter(email = request.POST['email']):
                messages.warning(request,'Email address already exists')
                return render(request,'register.html')
            
            User.objects.create(
                username=request.POST['username'],
                email=request.POST['email'],
                password=make_password(request.POST['password'])
            )
            return redirect('login')
        return render(request,'register.html')
        
    else:
        return redirect('home')


@login_required(login_url='lr')
def home(request):
    return render(request,'home.html')


@login_required(login_url='lr')
def interveiw(request):
    return render(request,'interview.html')


@login_required(login_url='lr')
def exam(request):
    q = exam_model.objects.all()
    return render(request,'exam.html',{q:'q'})


@login_required(login_url='lr')
def greetings(request):
    res = render(request,'h.html')
    return res
@login_required(login_url='lr')
def runcode(request):
    if request.method == "POST":
        codeareadata = request.POST['codearea']
        q = exam_model.objects.all()
        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(codeareadata)
            sys.stdout.close()
            sys.stdout = original_stdout
            output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout = original_stdout
            output = e
        return render(request,'h.html',{"code":codeareadata , "output":output , 'q':q})
    return render(request,'h.html')


@login_required(login_url='lr')
def codingsection_completed(request):
    return render(request,'codingsection_completed.html')

@login_required(login_url='lr')
def score(request):
    return render(request,'score.html')


@login_required(login_url='lr')
def about(request):
    return render(request,'about.html')


@login_required(login_url='lr')
def contactview(request):
    if request.method == 'POST':
        Contact_Model.objects.create(
            username=request.POST['username'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            desc=request.POST['desc'],
        )
        messages.success(request,'Thanks for contacting us.. Have a nice day...!!!') 
    return render(request,'contact.html')


def lr(request):
    if not request.user.is_authenticated:
        return render(request,'lr.html')
    else:
        return redirect('home')

def password_reset(request):
    if not request.user.is_authenticated:
        return render(request,'password_reset.html')
    else:
        return redirect('home')