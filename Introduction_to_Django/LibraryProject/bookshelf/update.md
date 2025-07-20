book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(f"Total books: {Book.objects.count()}")