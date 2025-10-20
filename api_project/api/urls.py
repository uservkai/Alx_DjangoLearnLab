from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all') #Registers the BookViewSet with the router

urlpatterns = [
    path('books/', BookList.as_view(), name = 'book_list'), #Maps the book
    path('api/', include(router.urls)), #Includes the router urls for BookViewSet(all CRUD operations)
]