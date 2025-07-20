from django.urls import path
from .views import list_books, LibraryDetailView

app_name = 'relationship_app'

urlpatterns = [
    # Function-based view for listing all books
    path('books/', list_books, name='list_books'),
    
    # Class-based view for library detail
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]