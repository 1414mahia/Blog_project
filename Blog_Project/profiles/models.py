from django.db import models
from author.models import Author

class Profiles(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()  # Changed from TimeField to TextField for descriptive content
    author = models.OneToOneField(Author, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.name