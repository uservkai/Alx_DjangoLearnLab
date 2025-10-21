from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all') #Registers the BookViewSet with the router

urlpatterns = [
    path('books/', BookList.as_view(), name = 'book_list'), #Maps the book
    path('api/', include(router.urls)), #Includes the router urls for BookViewSet(all CRUD operations)
    path('api-token-auth/', views.obtain_auth_token, name ='api_token_auth'), #Endpoint to obtain auth token
]