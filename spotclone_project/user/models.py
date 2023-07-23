from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = (("M", "male"), 
                      ("F", "female"), 
                      ("O", "other"))
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE)
    
    username = models.CharField(max_length=50)
    image = models.ImageField(blank=True, 
                              null=True)
    date_of_birth = models.DateTimeField(blank=True, 
                                         null=True)
    gender = models.CharField(
        max_length=6, 
        choices=GENDER_CHOICES, 
        blank=True, 
        null=True
    )
    email = models.EmailField()