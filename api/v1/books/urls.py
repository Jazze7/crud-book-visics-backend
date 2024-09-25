from django.urls import path
from api.v1.books import views


urlpatterns = [
    path('', views.books, name='list-books'),
    path('create-book/', views.create_book, name='create-book'),
    path('view-book/<int:pk>/', views.view_book, name='view-book'),
    path('update-book/<int:pk>/', views.update_book, name='update-book'),
    path('delete-book/<int:pk>/', views.delete_book, name='delete-book'),
]
