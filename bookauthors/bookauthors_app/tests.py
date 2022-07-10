from django.test import TestCase
from .models import Author, Book
from datetime import date


class AuthorTest(TestCase):
    def setUp(self):
        Author.objects.create(name='first', surname='first')

    def test1_count_books(self):
        """Тест функции при отсутствии книг, привязанных к автору"""
        first = Author.objects.get(name='first')
        self.assertEqual(first.count_books(), 0)

    def test2_count_books(self):
        """Тест функции при n - книг, привязанных к автору от 1 до 1000"""
        first = Author.objects.get(name='first')
        some_date = date(2012, 12, 14)
        for i in range(1000):
            Book.objects.create(name=f'book{i}', author=first, publication_date=some_date, pages_amount=33)
            self.assertEqual(first.count_books(), i+1)
