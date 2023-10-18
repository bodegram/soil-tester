from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Undisclosed', 'Undisclosed')
    )
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=GENDER, default='Undisclosed', max_length=1000)
    dob = models.DateField(blank=True, max_length=1000, null=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']