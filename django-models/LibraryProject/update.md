# Retrieve the book to update
book = Book.objects.get(title="1984")

# Display current title
print(f"Current title: {book.title}")

# Update the title
book.title = "Nineteen Eighty-Four"

# Save the changes to database
book.save()

# Display updated title
print(f"Updated title: {book.title}")