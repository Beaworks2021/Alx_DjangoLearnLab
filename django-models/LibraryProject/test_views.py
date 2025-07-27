#!/usr/bin/env python3
"""
Test script to verify the views are working correctly
"""
import os
import django
from django.test import Client
from django.urls import reverse

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Book, Library

def test_views():
    """Test the function-based and class-based views"""
    client = Client()
    
    print("Testing Function-based View (list_books)...")
    try:
        # Test the function-based view with proper headers
        response = client.get('/relationship/books/', HTTP_HOST='localhost')
        print(f"Status Code: {response.status_code}")
        print(f"Template Used: {response.templates[0].name if response.templates else 'No template'}")
        
        if response.status_code == 200:
            print("✅ Function-based view is working correctly!")
        else:
            print("❌ Function-based view has an issue")
            
    except Exception as e:
        print(f"❌ Error testing function-based view: {e}")
    
    print("\nTesting Class-based View (library_detail)...")
    try:
        # Get the first library
        library = Library.objects.first()
        if library:
            # Test the class-based view with proper headers
            response = client.get(f'/relationship/library/{library.id}/', HTTP_HOST='localhost')
            print(f"Status Code: {response.status_code}")
            print(f"Template Used: {response.templates[0].name if response.templates else 'No template'}")
            
            if response.status_code == 200:
                print("✅ Class-based view is working correctly!")
            else:
                print("❌ Class-based view has an issue")
        else:
            print("❌ No libraries found in database")
            
    except Exception as e:
        print(f"❌ Error testing class-based view: {e}")
    
    print("\nDatabase Content Summary:")
    print(f"Books: {Book.objects.count()}")
    print(f"Libraries: {Library.objects.count()}")
    
    # Show some sample data
    print("\nSample Books:")
    for book in Book.objects.all()[:3]:
        print(f"  - {book.title} by {book.author.name}")
    
    print("\nSample Libraries:")
    for library in Library.objects.all():
        print(f"  - {library.name} ({library.books.count()} books)")

if __name__ == "__main__":
    test_views() 