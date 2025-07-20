from django.urls import path
from .views import list_books, LibraryDetailView, home, books_by_author, LibraryListView

app_name = 'relationship_app'

urlpatterns = [
    # Home page
    path('', home, name='home'),
    
    # Function-based view for listing all books
    path('books/', list_books, name='list_books'),
    
    # Class-based view for library detail
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Additional views for better functionality
    path('libraries/', LibraryListView.as_view(), name='library_list'),
    path('author/<int:author_id>/books/', books_by_author, name='author_books'),
]