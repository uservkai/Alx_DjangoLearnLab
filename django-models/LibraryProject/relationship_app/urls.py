from django.urls import path
from . import views

urlpatterns = [
    path('list_books/', views.book_list, name = 'book_list_fbv'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name = 'library_detail'),
]