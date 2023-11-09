from django.shortcuts import render, redirect
from django.contrib import messages, auth
from app.models import *
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        next = request.GET.get('next')
        user = auth.authenticate(request, username=email, password=password)
        if user is not None:
            auth.login(request, user)
            if request.user.account_type == 'Customer':
                return redirect('dashboard')
            
           
            
            return redirect('user:dashboard')
                      
        
        else:
            messages.error(request, 'Invalid credential')
    
    return render(request, 'user/login.html')


def dashboard(request):
    if not request.user.account_type == "Admin":
        return redirect("login")
   
    
    return render(request, 'user/dashboard.html')


def tests(request):
    query = Test.objects.all()
    return render(request, 'user/tests.html', {"tests": query})


def test(request, slug):
    query =  Test.objects.get(test_id=slug)
    return render(request, 'user/test.html', {"test": query})


def generateResult(request, slug):
    query =  Test.objects.get(test_id=slug)
    if request.method == 'POST':
        report = request.POST.get('report')
        result = Result(test_result=query, report=report)
        result.save()
    
    
    return render(request, 'user/generate.html', {"test": query})


    
    
