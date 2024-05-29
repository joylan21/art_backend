# admin.py

from django.contrib import admin
from .models import Author, Art, Category

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', 'description')

@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'address')
    search_fields = ('title', 'category__name', 'address')
    list_filter = ('category',)  # Allows filtering by category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
