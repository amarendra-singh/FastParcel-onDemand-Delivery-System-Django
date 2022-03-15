from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #check if logged user has a customer if not it will add one 
    avatar = models.ImageField(upload_to='customer/avatars/', blank=True, null=True) #display default avatar if user have one

    def __str__(self):
        
        return self.user.get_full_name()