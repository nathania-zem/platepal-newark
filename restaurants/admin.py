from django.contrib import admin
from .models import Restaurant, Feedback, BusinessRequest, PromotionRequest, Suggestion

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'cuisine', 'price_range', 'is_featured']
    list_filter = ['cuisine', 'is_featured']
    list_editable = ['is_featured']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'restaurant', 'rating', 'created_at']
    list_filter = ['restaurant', 'rating']

@admin.register(BusinessRequest)
class BusinessRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'cuisine', 'email', 'submitted_at']

@admin.register(PromotionRequest)
class PromotionRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'submitted_at']

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ['suggestion', 'submitted_at']
