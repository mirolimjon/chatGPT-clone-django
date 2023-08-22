from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import messages
# Create your views here.


def loginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.filter(email=email).exists()

            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('chatview')
            else:
                messages.error("Ooops, username or password does not exists")
        except:
            messages.warning(request, "Username does not exists, If you have an account please move on registration page!")
    return render(request, 'accounts/login.html')

def logoutUser(request):
    logout(request)
    messages.warning(request, "You have logged out succesfully")
    return redirect('login')


def registerUser(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username already exists, please choose another one.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Emai; already exists, please choose another one.')
                return redirect('register')
            else:
                new_user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password1
                )
                new_user.save()
                messages.info(request, "User created successfully, Please login to our system.")
                return redirect('login')
        else:
            messages.error(request, "Passowords are different, They should be same!")
            return redirect('register')
    return render(request, 'accounts/sign-up.html')