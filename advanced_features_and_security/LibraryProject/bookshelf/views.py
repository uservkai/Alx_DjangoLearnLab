from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookForm
from .models import Book
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required

# Create your views here.
def index(request):
    return HttpResponse("Welcome to my bookshelf")

#enforcing permissions in views
@permission_required('bookshelf.can_view', raise_exception=True)
def can_view_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books':books})

@permission_required('bookshelf.can_create', raise_exception=True)
def can_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_books')
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def can_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('list_books')
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})