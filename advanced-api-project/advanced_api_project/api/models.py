from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.StringField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.StringField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"