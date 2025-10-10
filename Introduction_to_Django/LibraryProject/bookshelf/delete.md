#deleting a book
Book.objects.get(title = "Nineteen Eighty-Four").delete()

#Expected output
(1, {'bookshelf.Book': 1})
<QuerySet []>