from bookshelf.models import Book
# Retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Display book before deletion
print(f"Book to delete: {book}")
print(f"Book ID: {book.id}")

# Delete the book
book.delete()

# Confirm deletion by checking total count
total_books = Book.objects.count()
print(f"Total books after deletion: {total_books}")