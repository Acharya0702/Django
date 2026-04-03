from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'home.html')

def register_view(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    pass
