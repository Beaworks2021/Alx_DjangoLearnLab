"""
Sample queries demonstrating Django ORM relationships
Run this script in Django shell: python manage.py shell
Then: exec(open('relationship_app/query_samples.py').read())
"""

from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    """
    Query all books by a specific author using ForeignKey relationship
    """
    try:
        # Method 1: Using filter on Book model
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        
        print(f"\n=== Books by {author_name} ===")
        for book in books_by_author:
            print(f"- {book.title}")
        
        # Method 2: Using reverse relationship (more efficient)
        books_reverse = author.books.all()
        print(f"\nUsing reverse relationship:")
        for book in books_reverse:
            print(f"- {book.title}")
            
        return books_by_author
        
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return None


def list_all_books_in_library(library_name):
    """
    List all books in a library using ManyToMany relationship
    """
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        
        print(f"\n=== Books in {library_name} ===")
        for book in books_in_library:
            print(f"- {book.title} by {book.author.name}")
        
        # Alternative: Query from Book model
        # books_in_library_alt = Book.objects.filter(libraries=library)
        
        return books_in_library
        
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None


def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library using OneToOne relationship
    """
    try:
        library = Library.objects.get(name=library_name)
        
        # Method 1: Access through reverse relationship
        librarian = library.librarian
        print(f"\n=== Librarian for {library_name} ===")
        print(f"Librarian: {librarian.name}")
        
        # Method 2: Query from Librarian model
        librarian_alt = Librarian.objects.get(library=library)
        print(f"Alternative query: {librarian_alt.name}")
        
        return librarian
        
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")
        return None


def create_sample_data():
    """
    Create sample data to test the queries
    """
    print("Creating sample data...")
    
    # Create authors
    author1, created = Author.objects.get_or_create(name="J.K. Rowling")
    author2, created = Author.objects.get_or_create(name="George Orwell")
    author3, created = Author.objects.get_or_create(name="Jane Austen")
    
    # Create books
    book1, created = Book.objects.get_or_create(
        title="Harry Potter and the Philosopher's Stone", 
        author=author1
    )
    book2, created = Book.objects.get_or_create(
        title="Harry Potter and the Chamber of Secrets", 
        author=author1
    )
    book3, created = Book.objects.get_or_create(
        title="1984", 
        author=author2
    )
    book4, created = Book.objects.get_or_create(
        title="Animal Farm", 
        author=author2
    )
    book5, created = Book.objects.get_or_create(
        title="Pride and Prejudice", 
        author=author3
    )
    
    # Create libraries
    library1, created = Library.objects.get_or_create(name="Central Library")
    library2, created = Library.objects.get_or_create(name="Community Library")
    
    # Add books to libraries (ManyToMany relationship)
    library1.books.add(book1, book2, book3, book5)
    library2.books.add(book3, book4, book5)
    
    # Create librarians
    librarian1, created = Librarian.objects.get_or_create(
        name="Alice Johnson", 
        library=library1
    )
    librarian2, created = Librarian.objects.get_or_create(
        name="Bob Smith", 
        library=library2
    )
    
    print("Sample data created successfully!")


def run_all_queries():
    """
    Run all sample queries with the created data
    """
    print("Running all sample queries...\n")
    
    # Query all books by a specific author
    query_all_books_by_author("J.K. Rowling")
    query_all_books_by_author("George Orwell")
    
    # List all books in a library
    list_all_books_in_library("Central Library")
    list_all_books_in_library("Community Library")
    
    # Retrieve the librarian for a library
    retrieve_librarian_for_library("Central Library")
    retrieve_librarian_for_library("Community Library")


# Additional advanced queries for demonstration
def advanced_queries():
    """
    Additional complex queries demonstrating Django ORM capabilities
    """
    print("\n=== Advanced Queries ===")
    
    # Find all libraries that have books by a specific author
    author_name = "George Orwell"
    libraries_with_orwell = Library.objects.filter(books__author__name=author_name).distinct()
    print(f"\nLibraries with books by {author_name}:")
    for library in libraries_with_orwell:
        print(f"- {library.name}")
    
    # Find all authors who have books in a specific library
    library_name = "Central Library"
    authors_in_library = Author.objects.filter(books__libraries__name=library_name).distinct()
    print(f"\nAuthors with books in {library_name}:")
    for author in authors_in_library:
        print(f"- {author.name}")
    
    # Count books per author
    from django.db.models import Count
    authors_with_book_count = Author.objects.annotate(book_count=Count('books'))
    print(f"\nBooks per author:")
    for author in authors_with_book_count:
        print(f"- {author.name}: {author.book_count} books")


if __name__ == "__main__":
    # Uncomment the lines below to run when executing this script
    # create_sample_data()
    # run_all_queries()
    # advanced_queries()
    pass