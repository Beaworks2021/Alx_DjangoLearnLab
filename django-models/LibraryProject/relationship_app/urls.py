from django.urls import path
from .views import list_books


app_name = 'relationship_app'

urlpatterns = [
    # Home page
    path('', views.home_view, name='home'),
    
    # Function-based view for listing all books
    path('books/', views.list_books, name='list_books'),
    
    # Class-based view for library detail
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Alternative function-based view for library detail (optional)
    path('library/<int:pk>/function/', views.library_detail_function, name='library_detail_function'),
    
    # Additional views for better functionality
    path('libraries/', views.LibraryListView.as_view(), name='library_list'),
    path('author/<int:author_id>/books/', views.author_books, name='author_books'),
]