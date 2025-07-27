from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Library, Author, Librarian

# Home view (no authentication required)
def home_view(request):
    """
    Home view that displays welcome message and navigation
    """
    return render(request, 'relationship_app/home.html')

# Function-based view to list all books (requires authentication)
@login_required
def list_books(request):
    """
    Function-based view that lists all books stored in the database.
    Renders a list of book titles and their authors.
    Requires user authentication.
    """
    books = Book.objects.all().select_related('author')  # Optimize query with select_related
    
    # Render HTML template
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display library details (requires authentication)
class LibraryDetailView(LoginRequiredMixin, DetailView):
    """
    Class-based view that displays details for a specific library,
    listing all books available in that library.
    Requires user authentication.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    login_url = '/relationship/login/'
    
    def get_context_data(self, **kwargs):
        """
        Add additional context data if needed
        """
        context = super().get_context_data(**kwargs)
        # The library and its books are automatically available in the template
        # through the DetailView's default behavior
        return context


# Authentication Views

def register_view(request):
    """
    View for user registration
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after successful registration
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('relationship_app:list_books')
    else:
        form = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})





