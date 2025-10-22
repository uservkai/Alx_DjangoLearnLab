from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorListView, BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView 
from rest_framework.authtoken import views

router = DefaultRouter() #Creates a router for BookViewSet
router.register(r'books', BookViewSet, basename='book') 

urlpatterns = [
    path('api/books', include(router.urls)), #Includes the router urls for BookViewSet(all CRUD operations)
    path('api/authors/', AuthorListView.as_view(), name='author-list'), #Lists all authors
    path('api/booklist/', BookListView.as_view(), name = 'book-list'), #Lists all books
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),#Retrieves details of a specific book by its ID
    path('api/books/create/', BookCreateView.as_view(), name='book-create'), #Adds a new book
    path('api/books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'), #Updates an existing book
    path('api/books/delete/<int:pk>/', BookDeleteView.as_view(), name='bok-delete'), #Removes a book 
]