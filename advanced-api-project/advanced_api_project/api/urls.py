from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorListView 
from rest_framework.authtoken import views

router = DefaultRouter() #Creates a router for BookViewSet
router.register(r'books', BookViewSet, basename='book') 

urlpatterns = [
    path('api/books', include(router.urls)), #Includes the router urls for BookViewSet(all CRUD operations)
    path('api/authors/', AuthorListView.as_view(), name='author-list'), #Lists all authors
]