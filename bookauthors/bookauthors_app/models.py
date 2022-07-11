from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=100)
    publication_date = models.DateField()
    pages_amount = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
