from django.contrib import admin
from .models import Author, Book
from django.db.models import Count


class BookInline(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(AuthorAdmin, self).get_queryset(request)
        return queryset.annotate(num_books=Count('book'))

    def count_books(self):
        return self.num_books

    list_display = ('surname', count_books)
    inlines = [BookInline, ]


admin.site.register(Author, AuthorAdmin)
