from django.shortcuts import render, redirect
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test

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


def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {'form':form})

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'
    
#role based views
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
