from django.urls import path
from .views import GenreListView, GenreDetailView, GenreCreateView

app_name = 'genres'

urlpatterns = [
    path('', GenreListView.as_view(), name='genre_list'),
    path('add/', GenreCreateView.as_view(), name='genre_add'),
    path('<int:pk>/', GenreDetailView.as_view(), name='genre_detail'),
]