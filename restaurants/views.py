from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Restaurant, Feedback
from .forms import FeedbackForm, BusinessRequestForm, PromotionRequestForm, SuggestionForm, RegisterForm

def home(request):
    featured = Restaurant.objects.filter(is_featured=True)[:3]
    return render(request, 'home.html', {'featured': featured})

def italian(request):
    restaurants = Restaurant.objects.filter(cuisine='italian')
    return render(request, 'italian.html', {'restaurants': restaurants})

def mexican(request):
    restaurants = Restaurant.objects.filter(cuisine='mexican')
    return render(request, 'mexican.html', {'restaurants': restaurants})

def indian(request):
    restaurants = Restaurant.objects.filter(cuisine='indian')
    return render(request, 'indian.html', {'restaurants': restaurants})

def other(request):
    restaurants = Restaurant.objects.filter(cuisine='other')
    return render(request, 'other.html', {'restaurants': restaurants})
def showAll(request):
    restaurants = Restaurant.objects.all()  
    return render(request, 'showAll.html', {'restaurants': restaurants})

@login_required
def submit_feedback(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.restaurant = restaurant
            feedback.user = request.user
            feedback.save()
    return redirect('home')

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_staff:
                return redirect('/admin')
            return redirect('home')
        else:
            error = 'Invalid username or password.'
    return render(request, 'login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'register.html', {'form': form})

def add_business(request):
    form = BusinessRequestForm()
    if request.method == 'POST':
        form = BusinessRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'add_business.html', {'success': True})
    return render(request, 'add_business.html', {'form': form})

def promotions(request):
    form = PromotionRequestForm()
    if request.method == 'POST':
        form = PromotionRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'promotions.html', {'success': True})
    return render(request, 'promotions.html', {'form': form})

def suggestions(request):
    form = SuggestionForm()
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'suggestions.html', {'success': True})
    return render(request, 'suggestions.html', {'form': form})

@staff_member_required
def feedback_report(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'feedback_report.html', {'feedbacks': feedbacks})
