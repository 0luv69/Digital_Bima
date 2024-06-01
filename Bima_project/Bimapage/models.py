from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify



class Appoinment(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    # opd= models.ForeignKey (Opd)
    Hospital_CHOICES= (
        ('H1', 'H1'),
        ('H2', 'H2'),
    )
    Hospital = models.CharField(max_length=20, choices=Hospital_CHOICES, default='H1')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # medicine_token = models.ForeignKey(Medicine_token)
    appoinment_status= models.BooleanField(default=True)



class Hospital(models.Model):
    registration_num= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hos_name= models.CharField(max_length=100)
    hos_address= models.CharField(max_length=200)
    Hos_type= (
        ('gov', 'government'),
        ('private', 'private'),
    )
    hos_type= models.CharField(max_length=30, choices=Hos_type, default= 'gov')


