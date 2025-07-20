from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Book, Library, Author, Librarian

# Function-based view to list all books
def list_books(request):
    """
    Function-based view that lists all books stored in the database.
    Renders a list of book titles and their authors.
    """
    books = Book.objects.all().select_related('author')  # Optimize query with select_related
    
    # For simple text output (uncomment if you want plain text instead of HTML)
    # book_list = []
    # for book in books:
    #     book_list.append(f"{book.title} by {book.author.name}")
    # return HttpResponse("<br>".join(book_list))
    
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

# Additional function-based views for more functionality
def list_libraries(request):
    """
    Function-based view to list all libraries
    """
    libraries = Library.objects.all()
    context = {'libraries': libraries}
    return render(request, 'relationship_app/list_libraries.html', context)

def list_authors(request):
    """
    Function-based view to list all authors and their book counts
    """
    from django.db.models import Count
    authors = Author.objects.annotate(book_count=Count('books')).order_by('name')
    context = {'authors': authors}
    return render(request, 'relationship_app/list_authors.html', context)

# Class-based ListView examples
class BookListView(ListView):
    """
    Alternative class-based view to list all books using ListView
    """
    model = Book
    template_name = 'relationship_app/book_list_view.html'
    context_object_name = 'books'
    ordering = ['title']  # Order books by title
    paginate_by = 10  # Add pagination (10 books per page)
    
    def get_queryset(self):
        """
        Optimize the query by selecting related author data
        """
        return Book.objects.select_related('author').order_by('title')

class LibraryListView(ListView):
    """
    Class-based view to list all libraries
    """
    model = Library
    template_name = 'relationship_app/library_list_view.html'
    context_object_name = 'libraries'
    ordering = ['name']

# View to show books by a specific author
def books_by_author(request, author_id):
    """
    Function-based view to show all books by a specific author
    """
    try:
        author = Author.objects.get(id=author_id)
        books = author.books.all()
        context = {
            'author': author,
            'books': books
        }
        return render(request, 'relationship_app/books_by_author.html', context)
    except Author.DoesNotExist:
        return HttpResponse("Author not found.", status=404)

# Home view for the app
def home(request):
    """
    Home page view showing summary statistics
    """
    from django.db.models import Count
    
    total_books = Book.objects.count()
    total_authors = Author.objects.count()
    total_libraries = Library.objects.count()
    total_librarians = Librarian.objects.count()
    
    # Get recent books
    recent_books = Book.objects.select_related('author').order_by('-id')[:5]
    
    context = {
        'total_books': total_books,
        'total_authors': total_authors,
        'total_libraries': total_libraries,
        'total_librarians': total_librarians,
        'recent_books': recent_books,
    }
    return render(request, 'relationship_app/home.html', context)