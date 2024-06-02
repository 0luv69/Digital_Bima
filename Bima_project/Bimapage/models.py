from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify
from datetime import datetime

class Patient(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    user_pic = models.ImageField(upload_to='user_pic')
    
    bima_no = models.CharField(max_length=50, unique=True)
    birth_date = models.DateField()
    address = models.TextField()
    district = models.CharField(max_length=100)
    ward_no = models.IntegerField()
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    def __str__(self):
        return self.user.username





class Hospital(models.Model):
    registration_num = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hos_name = models.CharField(max_length=100)
    hos_address = models.CharField(max_length=200)
    HOS_TYPE_CHOICES = (
        ('gov', 'government'),
        ('private', 'private'),
    )
    hos_type = models.CharField(max_length=30, choices=HOS_TYPE_CHOICES, default='gov')
    hos_Ph = models.CharField(max_length=100, default=0)
    hos_email = models.EmailField(max_length=254, null=True, blank=True)
    hos_web = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to='hospital', blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now)  
    updated_at = models.DateTimeField(auto_now=True)     

    def __str__(self):
        return self.hos_name

class Appoinment(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    Hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    specilization = models.CharField(max_length=200 )
    appoinment_status= models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Opd(models.Model):
    appoinment = models.ForeignKey(Appoinment, on_delete=models.CASCADE)
    token_num = models.IntegerField()
    checkup_estimeted_time= models.DateTimeField(blank=True, null=True)
    medicine_estimeted_time= models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Medicine(models.Model):
    med_name= models.CharField(max_length=100)
    med_disc= models.TextField()
    med_price = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CheckupResult(models.Model):
    opd = models.ForeignKey(Opd, on_delete=models.CASCADE)
    medicine = models.ManyToManyField(Medicine)
    result_discription = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MedicineStore(models.Model):
    checkupresult = models.ForeignKey(CheckupResult, on_delete=models.CASCADE)
    total=  models.FloatField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





