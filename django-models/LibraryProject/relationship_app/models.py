from django.db import models

class Author(models.Model):
    """Author model with a name field"""
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Book(models.Model):
    """Book model with title and ForeignKey relationship to Author"""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"
    
    class Meta:
        ordering = ['title']


class Library(models.Model):
    """Library model with name and ManyToMany relationship to Books"""
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Librarian(models.Model):
    """Librarian model with OneToOne relationship to Library"""
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')
    
    def __str__(self):
        return f"{self.name} - {self.library.name}"
    
    class Meta:
        ordering = ['name']