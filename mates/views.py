from requests import request
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

# Create your views here.

def login(request):
    if request.method == "POST" and 'signup' in request.POST:
        get_name = request.POST.get('name')
        get_uname = request.POST.get('uname')
        get_email = request.POST.get('email')
        get_passwd = request.POST.get('password')
        conf_passwd = request.POST.get('confpwd')
        get_dob = request.POST.get('dob')
        get_mobile = request.POST.get('mobile')
        get_gender = request.POST.get('optradio')

        if get_passwd == conf_passwd:
            fetch_user = signup.objects.filter(Username=get_uname)
            fetch_email = signup.objects.filter(Email=get_email)
            fetch_mobile = signup.objects.filter(Mobile=get_mobile)
            if fetch_user.exists():
                messages.info(request, "Username already exists")
                params = [get_name, '', get_email, get_passwd, conf_passwd, get_mobile, get_dob, 'checked', 'checked']
                if get_gender == 'male':
                    params[8]=''
                else:
                    params[7]=''
                return render(request, "login.html",{'params':params})
            else:
                if fetch_email.exists():
                    messages.info(request, "Email already exists")
                    params = [get_name, get_uname, '', get_passwd, conf_passwd, get_mobile, get_dob, 'checked', 'checked']
                    if get_gender == 'male':
                        params[8] = ''
                    else:
                        params[7] = ''
                    return render(request, "login.html")
                else:
                    if fetch_mobile.exists():
                        messages.info(request, "Mobile already exists")
                        params = [get_name, get_uname, get_email, get_passwd, conf_passwd, '', get_dob, 'checked',
                                  'checked']
                        if get_gender == 'male':
                            params[8] = ''
                        else:
                            params[7] = ''
                        return render(request, "login.html")
                    else:
                        my_new_sign_up = signup(Name=get_name,
                                                Username=get_uname,
                                                Mobile=get_mobile,
                                                Email=get_email,
                                                Password=get_passwd,
                                                Gender=get_gender,
                                                Dob=get_dob
                                                )
                        my_new_sign_up.save()
                        print("Datails saved to database")
                        messages.success(request, 'You are successfully signed up.')
                        return render(request, "login.html")
        else:
            messages.info(request, "Passwords do not match")
            params = [get_name, get_uname, get_email, '', '', get_mobile, get_dob, 'checked', 'checked']
            if get_gender == 'male':
                params[8] = ''
            else:
                params[7] = ''
            return render(request, "login.html", {'params': params})
    else:
        return render(request, "login.html")

def feed(request):
    if request.method =="POST" and 'login' in request.POST:
        get_email = request.POST.get('email')
        get_pwd = request.POST.get('password')
        remember = request.POST.get('check')

        fetch_user = signup.objects.filter(Email=get_email, Password=get_pwd)
        if fetch_user.exists():
            user_details = signup.objects.get(Email=get_email)
            if remember == "on":
                params = {'user_details': user_details}
                response = render(request, "feed.html", {'params': params})
                response.set_cookie('save', get_email)
                print('cookie has been set')
                return response
            else:
                params = {'user_details': user_details}
                return render(request, 'feed.html', {'params':params})
        else:
            messages.success(request, 'Wrong Username or Password.')
            return render(request, "login.html")


    else:
        if request.COOKIES.get('save'):
            user_details = signup.objects.get(Email=request.COOKIES.get('save'))
            params = {'user_details': user_details}
            return render(request, 'feed.html', {'params': params})
        elif request.COOKIES.get('sessionid'):
            return render(request, 'feed.html')
        else:
            return render(request, 'login.html')

def logout(request):
    if request.COOKIES.get('save'):
        response = render(request, "login.html")
        response.delete_cookie("save")
        print('cookie has been deleted')
    elif request.COOKIES.get('sessionid'):
        response = render(request, "login.html")
        response.delete_cookie("sessionid")
        print('cookie has been deleted')
    else:
        print('cookie is not deleted')
        response = render(request, "login.html")
    return response
