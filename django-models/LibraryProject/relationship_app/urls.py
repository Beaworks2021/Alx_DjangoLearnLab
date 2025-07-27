from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Home page
    path('', views.home_view, name='home'),
    
    # Authentication URLs using Django's built-in views
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html', http_method_names=['get', 'post']), name='logout'),
    
    # Function-based view for listing all books
    path('books/', views.list_books, name='list_books'),
    
    # Class-based view for library detail
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Role-based access control URLs
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]