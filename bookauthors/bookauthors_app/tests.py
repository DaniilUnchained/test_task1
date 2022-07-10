from django.test import TestCase
from .models import Author, Book
from datetime import date


class AuthorTest(TestCase):
    def setUp(self):
        Author.objects.create(name='first', surname='first')

    def test1_count_books(self):
        first = Author.objects.get(name='first')
        self.assertEqual(first.count_books(), 0)

    def test2_count_books(self):
        first = Author.objects.get(name='first')
        some_date = date(2012, 12, 14)
        book1 = Book.objects.create(name='book1', author=first, publication_date=some_date, pages_amount=33)
        book2 = Book.objects.create(name='book2', author=first, publication_date=some_date, pages_amount=33)
        book3 = Book.objects.create(name='book3', author=first, publication_date=some_date, pages_amount=33)
        self.assertEqual(first.count_books(), 3)
