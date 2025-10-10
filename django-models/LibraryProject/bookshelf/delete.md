#deleting a book
Book.objects.get(title = "Nineteen Eighty-Four").delete()

from bookshelf.models import Book
book = Book.objects.get(title = "Nineteen Eighty-Four")
book.delete()

#Expected output
(1, {'bookshelf.Book': 1})
<QuerySet []>