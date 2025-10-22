from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

#Create your views here.
class AuthorListView(generics.ListAPIView): # lists all authors
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class BookViewSet(viewsets.ModelViewSet): # handles all CRUD operations for Book model
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookListView(generics.ListAPIView): #retrieves a list of all books
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # allows read-only access for unauthenticated users
    
class BookDetailView(generics.RetrieveAPIView): #retrieves details of a specific book by its ID
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # allows read-only access for unauthenticated users
    
class BookCreateView(generics.CreateAPIView): #adding a new book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication] # requires token authentication
    permission_classes = [IsAuthenticated] # only authenticated users can create books
    
    def perform_create(self, serializer):
        serializer.save() # triggers validation and saves the new book instance

class BookUpdateView(generics.UpdateAPIView): #updating and existing book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication] # requires token authentication
    permission_classes = [IsAuthenticated] # only authenticated users can update books]
    
    def perform_update(self, serializer):
        serializer.save() # triggers validation and saves the updated book instance
    
class BookDeleteView(generics.DestroyAPIView): #removing a book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication] # requires token authentication
    permission_classes = [IsAuthenticated] # only authenticated users can delete books
