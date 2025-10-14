from django.shortcuts import render, redirect
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def list_books(request):
    """Retrieves all books and renders a template displaying the list"""
    books = Book.objects.all() #fetches all book instances from the db
    context = {'list_books': books} #creates context dic with book list
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
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm (data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect ('index')
    else:
        form = AuthenticationForm() 
    return render(request, "relationship_app/login.html", {'form': form})

def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

def register_view(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {'form':form})