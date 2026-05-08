from django import forms
from .models import Feedback, BusinessRequest, PromotionRequest, Suggestion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comment']

class BusinessRequestForm(forms.ModelForm):
    class Meta:
        model = BusinessRequest
        fields = ['name', 'address', 'cuisine', 'email', 'description']

class PromotionRequestForm(forms.ModelForm):
    class Meta:
        model = PromotionRequest
        fields = ['name', 'email', 'reason']

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['suggestion']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
