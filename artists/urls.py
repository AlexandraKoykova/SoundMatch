from django.urls import path

from .views import (ArtistListView,ArtistDetailView,ArtistCreateView,ArtistUpdateView,ArtistDeleteView,)

app_name = 'artists'

urlpatterns = [
    path('', ArtistListView.as_view(), name='artist_list'),
    path('add/', ArtistCreateView.as_view(), name='artist_add'),
    path('<int:pk>/', ArtistDetailView.as_view(), name='artist_detail'),
    path('<int:pk>/edit/', ArtistUpdateView.as_view(), name='artist_edit'),
    path('<int:pk>/delete/', ArtistDeleteView.as_view(), name='artist_delete'),
]