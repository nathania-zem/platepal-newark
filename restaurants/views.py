from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

# Create your views here.
def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')


def italian(request):
    return render(request, 'italian.html')

def mexican(request):
    return render(request, 'mexican.html')

def indian(request):
    return render(request, 'indian.html')

def other(request):
    return render(request, 'other.html')

def showAall(request):
    return render(request, 'showAll.html')

def add_business(request):
    return render(request, 'add_business.html')

def promotions(request):
    return render(request, 'promotions.html')

def suggestions(request):
    return render(request, 'suggestions.html')

