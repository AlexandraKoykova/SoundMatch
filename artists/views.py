from django.urls import reverse_lazy
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView,)

from .models import Artist
from .forms import ArtistForm



from django.views.generic import ListView
from genres.models import Genre
from .models import Artist


class ArtistListView(ListView):
    model = Artist
    template_name = 'artists/artists-list.html'
    context_object_name = 'artists'

    def get_queryset(self):
        queryset = Artist.objects.all()

        search = self.request.GET.get('search', '').strip()
        genre = self.request.GET.get('genre', '')
        sort = self.request.GET.get('sort', '')

        if search:
            queryset = queryset.filter(
                stage_name__icontains=search
            )

        if genre:
            queryset = queryset.filter(
                genres__pk=genre
            )

        if sort == 'price_asc':
            queryset = queryset.order_by('booking_price')
        elif sort == 'price_desc':
            queryset = queryset.order_by('-booking_price')
        elif sort == 'name':
            queryset = queryset.order_by('stage_name')
        else:
            queryset = queryset.order_by('-created_at')

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['genres'] = Genre.objects.all()
        context['selected_search'] = self.request.GET.get('search', '')
        context['selected_genre'] = self.request.GET.get('genre', '')
        context['selected_sort'] = self.request.GET.get('sort', '')

        return context


class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artists/artist-detail.html'
    context_object_name = 'artist'


class ArtistCreateView(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'artists/artist-form.html'
    success_url = reverse_lazy('artists:artist_list')


class ArtistUpdateView(UpdateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'artists/artist-form.html'
    success_url = reverse_lazy('artists:artist_list')


class ArtistDeleteView(DeleteView):
    model = Artist
    template_name = 'artists/artist-confirm-delete.html'
    success_url = reverse_lazy('artists:artist_list')
from django.shortcuts import render

# Create your views here.
