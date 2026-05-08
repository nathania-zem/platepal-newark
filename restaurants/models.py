from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Restaurant(models.Model):
    CUISINE_CHOICES = [
        ('italian', 'Italian'),
        ('mexican', 'Mexican'),
        ('indian', 'Indian'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    price_range = models.CharField(max_length=10)
    image = models.ImageField(upload_to='restaurants/', blank=True, null=True)
    cuisine = models.CharField(max_length=20, choices=CUISINE_CHOICES)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def avg_rating(self):
        feedbacks = self.feedbacks.all()
        if feedbacks:
            return round(sum(f.rating for f in feedbacks) / len(feedbacks), 1)
        return None

class Feedback(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='feedbacks')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.restaurant.name} - {self.rating}/5'

class BusinessRequest(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    cuisine = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PromotionRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    reason = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Suggestion(models.Model):
    suggestion = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.suggestion[:50]
