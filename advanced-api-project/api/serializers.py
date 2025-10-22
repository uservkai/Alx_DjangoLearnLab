from .models import Book, Author
from rest_framework import serializers

# Serializers --- handles data conversion and validation---.
class BookSerializer(serializers.ModelSerializer): # converts Book model instances to JSON
    class Meta:
        model = Book
        fields = '__all__'
        
    def validate_publication_year(self, value):
        if value > 2025:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer): # converts Author model instances to JSON
    books = BookSerializer(many=True, read_only=True) # nested serialization to include author's books
        
    class Meta:
        model = Author
        fields = ['name', 'books']