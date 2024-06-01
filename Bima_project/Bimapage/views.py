from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User





def homepage(request):
    return render(request, 'pages/index.html')






def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        uname = request.POST.get('uname')
        password = request.POST.get('pwrd')
        user_obj = User.objects.filter(username = uname)
        if not user_obj.exists():
            messages.warning(request, "UserName seems New, Plz First register.")
            return redirect(request.path_info)

        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, "Opps!! Your account is not Verified till yet, check ur mail")
            return HttpResponseRedirect(request.path_info)
        
        messages.warning(request, "Opps, Wrong credentials. Try again")
        return HttpResponseRedirect(request.path_info)
    return render(request,'auth_page/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pwrd')
        user_type = request.POST.get('user_type')

        print(password)
        user_obj = User.objects.filter(username = uname)
        if user_obj.exists():
            messages.warning(request, f"User with {uname} is already reigstered")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create(first_name= first_name, last_name= last_name, email = email, username = uname)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, "Success, Now lets see Weather you are real, Check your mail plz")
        return HttpResponseRedirect(request.path_info)

    return render(request, 'auth_page/register.html')

def logout_page(request):
    logout(request)      
    messages.success(request, "Loged out ")
    
    return redirect('/auth/login')