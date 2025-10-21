from django.db import models

# Create your models here.
class Author(models.Model): # stores author details and links to their books
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Book(models.Model): # represents a book with title, publication year and links to its author
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books') # establishes a many to one connection with Author
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"