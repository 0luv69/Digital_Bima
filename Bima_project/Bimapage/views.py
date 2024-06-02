from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone
from datetime import timedelta

def check_new_day():
    lst_appoinment=Appoinment.objects.last()
    if lst_appoinment:
        last_date = lst_appoinment.created_at.date()
        current_date = timezone.now().date()
        print(current_date, last_date)
        if last_date != current_date:
            return 1
        else:
            return 0
    return 1

def homepage(request):
    hospitals = Hospital.objects.all()
    opd, latest_Opd=None,None
    
    if request.user.is_authenticated:
        opd = Opd.objects.filter(appoinment__user=request.user)
        latest_Opd= opd.last()
    else:
        messages.info(request, "Plz Create Account or Log in First")

    
    context = {'hospitals':hospitals, 'opd':opd, 'latest_Opd':latest_Opd}
    return render(request, 'pages/index.html',context)

@login_required(login_url="login")
def appoinment(request):
    if request.method == 'POST':
        hospital_name = request.POST.get('hospital')
        doctor_type = request.POST.get('doctor_type')
        hospital = get_object_or_404(Hospital, hos_name=hospital_name)

        if check_new_day():
            new_token = 1
        else:
            last_token_num= Opd.objects.last().token_num
            new_token = last_token_num +1
        checkup_estimeted_time = timezone.now() + timedelta(minutes=15)
        medicine_estimeted_time= checkup_estimeted_time +  timedelta(minutes=20)
        

        appoinment= Appoinment.objects.create(user=request.user, Hospital=hospital, specilization=doctor_type)
        opd = Opd.objects.create(appoinment=appoinment, token_num=new_token,
                                 checkup_estimeted_time=  checkup_estimeted_time,
                                  medicine_estimeted_time= medicine_estimeted_time )

        messages.success(request, 'Succefully added')
    return redirect(homepage)
    
def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = uname)
        if not user_obj.exists():
            messages.warning(request, "UserName seems New, Plz First register.")
            return redirect(request.path_info)
        user_auth = authenticate(username = uname, password= password)
        if user_auth:
            login(request, user_auth)
            messages.success(request, "Logged in Success")
            return redirect('home')
        
        
        messages.warning(request, "Opps, Wrong credentials. Try again")
        return HttpResponseRedirect(request.path_info)
    return render(request,'pages/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        gender = request.POST.get('gender')
        BimaNumber = request.POST.get('BimaNumber')
        date_of_birth = request.POST.get('Date')
        Address = request.POST.get('Address')
        District = request.POST.get('District')
        Ward = request.POST.get('Ward')
        pic = request.FILES.getlist('images')

        user_obj = User.objects.filter(username = username)
        if user_obj.exists():
            messages.warning(request, f"User with {username} is already reigstered")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create(first_name= full_name, email = email, username = username)
        user_obj.set_password(password)
        user_obj.save()

        #patient
        patient_obj= Patient.objects.create(user =user_obj,user_pic= pic, bima_no=BimaNumber,
                                            birth_date= date_of_birth,address=Address,district= District,
                                               gender=gender, ward_no= Ward )

        messages.success(request, "Success, Now lets see Weather you are real, Check your mail plz")
        return HttpResponseRedirect(request.path_info)

    return render(request, 'pages/register.html')

@login_required(login_url="login")
def logout_page(request):
    logout(request)      
    messages.success(request, "Loged out ")
    return redirect('login')