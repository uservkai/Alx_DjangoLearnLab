#Query all books by a specific author
from relationship_app.models import Author, Book

author=Author.objects.get(name=author_name)
objects.filter(author=author)

#List all books on a library
from relationship_app.models import Library

library=Library.objects.get(name=library_name)
books = library.books.all()

for book in books:
    print(f"{book.title} by {book.author.name}")
    
#Retrieve librarian from a library
from relationship_app.models import Librarian

librarian = Librarian.objects.get(name=librarian_name)