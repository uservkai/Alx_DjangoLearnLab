from django.shortcuts import render
from .models import Library, Book
from django.views.generic.detail import DetailView

# Create your views here.
def book_list(request):
    """Retrieves all books and renders a template displaying the list"""
    books = Book.objects.all() #fetches all book instances from the db
    context = {'book_list': books} #creates context dic with book list
    return render (request, "relationship_app/list_books.html", context)
    
class LibraryDetailView(DetailView):
    """ class based view for listing all books available in the db"""
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context["books"] = library.books.all() 
        return context
    