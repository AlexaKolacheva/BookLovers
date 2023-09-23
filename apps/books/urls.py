from django.urls import path
from . import views

urlpatterns = [

    path('', views.BookListView.as_view(), name='book_list'),
    path('detail/<int:book_id>', views.BookDetailView.as_view(), name='book_detail'),
    path('book_genre', views.book_genre, name='book_genre'),
    path('get_book_by_genre/<int:genre_id>/', views.get_book_by_genre, name='get_book_by_genre'),
    path('author_book', views.author_book, name='author_book'),
    path('get_book_by_author/<int:author_id>/', views.get_book_by_author, name='get_book_by_author'),

]

