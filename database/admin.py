from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "places_to_purchase", "lowest_price")

admin.site.register(Book, BookAdmin)
