#Query all books by a specific author
from relationship_app.models import Author, Book

books = Book.objects.filter(author__name = "George")

#List all books on a library
from relationship_app.models import Library

library = Library.objects.get(name = "abc")
books = library.books.all()

for book in books:
    print(f"{book.title} by {book.author.name}")
    
#Retrieve librarian from a library
from relationship_app.models import Librarian

librarian = Librarian.objects.get(name = "abc")