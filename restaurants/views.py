from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

# Create your views here.
def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')