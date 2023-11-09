from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Undisclosed', 'Undisclosed')
    )
    
    ACCOUNT_TYPE = (
        ('Customer', 'Customer'),
        ('Admin', 'Admin')
    )
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=GENDER, default='Undisclosed', max_length=1000)
    dob = models.DateField(blank=True, max_length=1000, null=True)
    account_type = models.CharField(max_length=1000, null=True, choices=ACCOUNT_TYPE)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
    
class Test(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    )
    name = models.CharField(max_length=1000, null=True)
    date_created = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=1000, null=True)
    status = models.CharField(max_length=1000, null=True, choices=STATUS, default='Pending')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    home_address = models.CharField(max_length=1000, null=True)
    state = models.CharField(max_length=1000, null=True)
    test_option = models.CharField(max_length=100, null=True)
    test_id = models.CharField(max_length=100, null=True, unique=True)
    scheduleDate = models.DateField(null=True)
    
class Result(models.Model):
    test_result = models.ForeignKey(Test, on_delete=models.CASCADE)
    _test = models.CharField(max_length=1000, null=True)
    report = models.TextField(null=True)