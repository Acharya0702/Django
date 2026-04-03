from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Register
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error':'username already exists!'})
        user = User.objects.create_user(
            username=username, 
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            password=password
            )
        user.save()
        return redirect('login')
    return render(request, 'register.html')


# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error':'Invalid Credentials!'})
    return render(request, 'login.html')

# Dashboard (protected)
@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')
