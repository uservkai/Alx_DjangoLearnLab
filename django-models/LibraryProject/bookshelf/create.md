#Create a book instance
from bookshelf.models import Book

book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)
book.save()

#Expected output
<QuerySet [<Book: Book : 1984 by George Orwell (1949)>]>