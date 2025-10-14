from django.urls import path
from . import views
from .views import list_books, login_view, logout_view, register_view

urlpatterns = [
    path('list_books/', views.list_books, name = 'list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name = 'library_detail'),
    path('login/',login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name= 'register')
]