from django.urls import path, include
from main.views import show_main, search_books, search_books_blank

app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
    path('search-books/', search_books, name='search_books'),
    path('search-books-blank/', search_books_blank, name='search_books'),
]
