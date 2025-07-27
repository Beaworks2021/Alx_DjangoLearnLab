from django.urls import path
from .views import home_view, list_books, LibraryDetailView, register_view, login_view, logout_view

app_name = 'relationship_app'

urlpatterns = [
    # Home page
    path('', home_view, name='home'),
    
    # Authentication URLs
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    
    # Function-based view for listing all books
    path('books/', list_books, name='list_books'),
    
    # Class-based view for library detail
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]