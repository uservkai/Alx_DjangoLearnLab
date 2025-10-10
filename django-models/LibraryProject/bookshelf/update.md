#updating book
Book.objects.filter(title = "1984").update(title = "Nineteen Eighty-Four")

#or
book = Book.objects.get(title = "1984")
book.title = "Nineteen Eighty-Four"
book.save()

#Expected output
<QuerySet [<Book: Book : Nineteen Eighty-Four by George Orwell (1949)>]>