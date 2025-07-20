from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Book, Library, Author, Librarian

# Function-based view to list all books
def list_books(request):
    """
    Function-based view that lists all books stored in the database.
    Renders a list of book titles and their authors.
    """
    books = Book.objects.all().select_related('author')  # Optimize query with select_related
    
    # Render HTML template
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display library details
class LibraryDetailView(DetailView):
    """
    Class-based view that displays details for a specific library,
    listing all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        """
        Add additional context data if needed
        """
        context = super().get_context_data(**kwargs)
        # The library and its books are automatically available in the template
        # through the DetailView's default behavior
        return context