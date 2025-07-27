from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home_view, list_books, LibraryDetailView, register_view

app_name = 'relationship_app'

urlpatterns = [
    # Home page
    path('', home_view, name='home'),
    
    # Authentication URLs using Django's built-in views
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('register/', register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html', http_method_names=['get', 'post']), name='logout'),
    
    # Function-based view for listing all books
    path('books/', list_books, name='list_books'),
    
    # Class-based view for library detail
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]