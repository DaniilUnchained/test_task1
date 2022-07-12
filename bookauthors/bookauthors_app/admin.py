from django.contrib import admin
from .models import Author, Book
from django.db.models import Count


class BookInline(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):

    def count_books(self):
        """Запрос к БД подсчитывающий кол-во книг для каждого автора"""
        nums_set = Author.objects.annotate(num_books=Count('book'))
        return nums_set[self.id-1].num_books

    list_display = ('surname', count_books)
    inlines = [BookInline, ]


admin.site.register(Author, AuthorAdmin)
