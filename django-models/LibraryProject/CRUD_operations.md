# Import the Book model
from bookshelf.models import Book

# Retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")
print(f"Book to delete: {book}")
print(f"Book ID: {book.id}")

# Delete the book
book.delete()

# Confirm deletion
print(f"Total books after deletion: {Book.objects.count()}")
print(f"All books: {list(Book.objects.all())}")

# Verify deletion by trying to retrieve the deleted book
try:
    deleted_book = Book.objects.get(title="Nineteen Eighty-Four")
    print("ERROR: Book still exists!")
except Book.DoesNotExist:
    print("SUCCESS: Book has been deleted from the database")