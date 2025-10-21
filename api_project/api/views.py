from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets, generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # authentication required
    
class BookListView(APIView): 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] # authentication required
    
    # only authenticated users can view books
    def get(self, request): 
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

class BookCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    # only admin users can create books
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) #Created
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Bad Request
    
            