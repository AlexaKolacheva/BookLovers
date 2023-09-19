from django.db import models
from apps.accounts.models import CustomUser


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(blank=True)
    death_date = models.DateField(blank=True)

    @property
    def count_books(self):
        return self.author_books.all().count()

    def __str__(self):
        return self.first_name

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author, related_name='author_books')
    genre = models.ManyToManyField(Genre, related_name='genre_books')
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    discription = models.TextField()


    def __str__(self):
        return self.title
