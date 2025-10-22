from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

#Create your views here.
class AuthorListView(generics.ListAPIView): # lists all authors
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class BookViewSet(viewsets.ModelViewSet): # handles all CRUD operations for Book model
    queryset = Book.objects.all()
    serializer_class = BookSerializer