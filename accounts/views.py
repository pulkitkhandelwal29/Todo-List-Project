from django.shortcuts import render,redirect

#Helps to create predefined forms (signup form--username,password1,password2)
from django.contrib.auth.forms import UserCreationForm

#Create user
from django.contrib.auth.models import User
#Helps to login,Logout
from django.contrib.auth import login,logout

#Integrity lets you uniquely identify column in database, if not uniquely identify IntegrityError is returned
from django.db import IntegrityError


# Create your views here.
def signupuser(request):
    #If signup link is opened, it's a GET request
    if request.method == 'GET':
        return render(request,'accounts/signup.html',{'form':UserCreationForm()})
    else:
        #Otherwise the request is POST(posting the details and clicking on sign up button)
        #Retrieving details
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if  password1 == password2:
            # Create a new user
            try:
                user = User.objects.create_user(username = username , password = password1)
                #Saving user into database
                user.save()
                #As soon as user signs up, it is logged in
                login(request,user)
                #After logging in, we need to show some page (currenttodos.html),redirecting to webpage
                return redirect('currenttodos')

            except IntegrityError:
                return render(request,'accounts/signup.html',{'form':UserCreationForm(),'error':'Username already exists!'})
        else:
            #If passwords does not match (return the same page again with additional details)
            return render(request,'accounts/signup.html',{'form':UserCreationForm(),'error':'Passwords didn\'t match'})


def logoutuser(request):
    if request.method == 'POST':
        #Logouts the user
        logout(request)
        #returning to specific webpage
        return redirect('home')
