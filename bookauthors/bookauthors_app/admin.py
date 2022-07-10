from django.contrib import admin
from .models import Author, Book


class BookInline(admin.TabularInline):
    model = Book
    
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('surname', 'count_books')
    inlines = [BookInline,]


admin.site.register(Author, AuthorAdmin)