from django.db import models
from categories.models import Category
from author.models import Author
# Create your models here.

class Post(models.Model):
    title =models.CharField(max_length=50)
    content =models.TextField()
    category =models.ManyToManyField(Category)
    #ekta post multiple categorir modde thakte pare abr ekta caterory multiple post athakte pare
    author =models.ForeignKey(Author,on_delete=models.CASCADE) # author delete hole sob post o delete hoye jabez 
    
    def __str__(self):
        return self.title