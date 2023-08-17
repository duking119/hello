from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# class Book(models.Model):
#     title = models.CharField(max_length=50)
#     rating = models.IntegerField(null= True,validators=[MinValueValidator(1), MaxValueValidator(5)])
#     autor = models.CharField(null= True,max_length=100)
#     is_bestselling = models.BooleanField(default=False)

class Book_new(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(null= True,validators=[MinValueValidator(1), MaxValueValidator(5)])
    autor = models.CharField(null= True,max_length=100)
    is_bestselling = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.title} ({self.rating})"