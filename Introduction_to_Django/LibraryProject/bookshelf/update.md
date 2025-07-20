book = Book.objects.get(title="1984")
print(f"Current title: {book.title}")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated title: {book.title}")