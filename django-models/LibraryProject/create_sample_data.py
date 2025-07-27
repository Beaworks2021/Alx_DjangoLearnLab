#!/usr/bin/env python3
"""
Script to create sample data for testing the relationship_app views
"""
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    """Create sample authors, books, libraries, and librarians"""
    
    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George R.R. Martin")
    author3 = Author.objects.create(name="J.R.R. Tolkien")
    
    # Create books
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="A Game of Thrones", author=author2)
    book4 = Book.objects.create(title="The Lord of the Rings", author=author3)
    book5 = Book.objects.create(title="The Hobbit", author=author3)
    
    # Create libraries
    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="University Library")
    
    # Add books to libraries
    library1.books.add(book1, book2, book3)
    library2.books.add(book3, book4, book5)
    
    # Create librarians
    librarian1 = Librarian.objects.create(name="Sarah Johnson", library=library1)
    librarian2 = Librarian.objects.create(name="Michael Brown", library=library2)
    
    print("Sample data created successfully!")
    print(f"Created {Author.objects.count()} authors")
    print(f"Created {Book.objects.count()} books")
    print(f"Created {Library.objects.count()} libraries")
    print(f"Created {Librarian.objects.count()} librarians")

if __name__ == "__main__":
    create_sample_data() 