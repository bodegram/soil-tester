from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from .models import *
from django.contrib.auth.hashers import make_password
from random import randint
from django.core.paginator import Paginator
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.
def home(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        next = request.GET.get('next')
        user = auth.authenticate(request, username=email, password=password)
        if user is not None:
            auth.login(request, user)
            
           
            
            return redirect('dashboard')
                      
        
        else:
            messages.error(request, 'Invalid credential')
    
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        password = request.POST.get('password')
        username = f'{fname} {randint(10, 90)}'
       
        
        
        if  email is not None and password is not None and fname is not None and lname is not None:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username already in use')
                
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email already in use')
                
            else:
                user = CustomUser(username=username, email=email, first_name=fname, last_name=lname, account_type='Customer')
                user.set_password(password)
                user.save()
                messages.success(request, 'Account successfully created, proceed to login.')
                return redirect('login')
        
        else:
            messages.error(request, 'Password does not match')
    return render(request, 'register.html')


def resetPassword(request):
    return render(request, 'resetPassword.html')

def dashboard(request):
   
    
    return render(request, 'dashboard.html')



def profile(request):
    
    return render(request, 'profile.html')




def changePassword(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if confirm_password == new_password:
            if old_password == request.user.password:
                user = CustomUser.objects.get(email=request.user)
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password successfully updated')
            
            else:
                messages.error(request, 'Incorrect password')
        
        else:
            messages.error(request, 'Password does not match')
    return render(request, 'changePassword.html')



def updateProfile(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        location = request.POST.get('location')
        dob = request.POST.get('dob')
        
        # Edit Profile
        user = CustomUser(email=request.user)
        user.first_name = fname
        user.last_name = lname
        user.location = location
        user.dob = dob
        user.save()
        messages.success(request, 'Profile successfully updated')
        
        
    return render(request, 'updateProfile.html')


def changeUsername(request):
    if request.method == 'POST':
        new_username = request.POST.get('new_username')
        password = request.POST.get('password')
        user = CustomUser(email=request.user)
        
        if password == user.password:
            if new_username == user.username:
                messages.error(request, 'use a new username')
                
            elif CustomUser.objects.filter(username=new_username).exists():
                messages.error(request, 'Username already in use')
                
            else:
                user.username = new_username
                user.save()
                messages.success(request, 'Username successfully updated')
        
        else:
            messages.error(request, 'Incorrect password')
        
        
    return render(request, 'changeUsername.html')



def changeEmail(request):
    if request.method == 'POST':
        new_email = request.POST.get('new_email')
        password = request.POST.get('password')
        user = CustomUser(email=request.user)
        
        if password == user.password:
            if new_email == user.email:
                messages.error(request, 'use a new email address')
                
            elif CustomUser.objects.filter(email=new_email).exists():
                messages.error(request, 'Email address already in use')
                
            else:
                user.email = new_email
                user.save()
                messages.success(request, 'Email address successfully updated')
        
        else:
            messages.error(request, 'Incorrect password')
        
        
    return render(request, 'changeEmail.html')



def logout(request):
    auth.logout(request)
    return redirect('login')




def test(request):
    return render(request, 'test.html')

def settings(request):
    return render(request, 'settings.html')

def createTest(request):
    if request.method == 'POST':
        test_option = request.POST.get('test_option')
        type = request.POST.get('type')
        home_address = request.POST.get('home_address')
        state = request.POST.get('state')
        name = request.POST.get('name')
        scheduleDate = request.POST.get('scheduleDate')
        test_id = randint(100000, 900000)
       
        if Test.objects.filter(user=request.user, test_id=test_id).exists():
            messages.error(request, 'An error occurred')
        else:
            query = Test(user=request.user, test_option=test_option, type=type, state=state, home_address=home_address, name=name, scheduleDate=scheduleDate, test_id=test_id)
            query.save()
            messages.success(request, 'Request being processed...')
        
    return render(request, 'soilPh.html')


def allTests(request):
    query = Paginator(Test.objects.filter(user=request.user).all(), 10)
    page = request.GET.get('page')
    tests  = query.get_page(page)
    return render(request, 'allTests.html', {"tests": tests})


def viewTest(request, id):
    try:
        test = Test.objects.get(test_id=id)
    except:
        return redirect('allTests')
    return render(request, 'viewTest.html', {"test": test})



def pdfResult(request, slug):
    query = Test.objects.get(test_id=slug)
    result = Result.objects.get(test_result=query)
    buff = io.BytesIO()
    c = canvas.Canvas(buff, pagesize=letter, bottomup=0)
    textObj = c.beginText()
    textObj.setTextOrigin(inch, inch)
    textObj.setFont('Helvetica', 14)
    lines = [
        'SOIL TRACKA',
        '',
        'User Information',
        f'Name: {request.user.email}',
        '',
        'Test Information',
        f'Test name: {query.name}',
        f'Test Option: {query.test_option}',
        f'Test Type: {query.type}',
        f'Date created: {query.date_created}',
        f'Test Status: {query.status}',
        f'Test Report: {result.report}',
        
    ]
    for line in lines:
        textObj.textLine(line)
        
    c.drawText(textObj)
    c.showPage()
    c.save()
    buff.seek(0)
    return FileResponse(buff, as_attachment=True, filename='result.pdf')