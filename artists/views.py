from django.urls import reverse_lazy
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView,)
from .models import Artist
from .forms import ArtistForm

class ArtistListView(ListView):
    model = Artist
    template_name = 'artists/artist_list.html'
    context_object_name = 'artists'

class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artists/artist_detail.html'
    context_object_name = 'artist'

class ArtistCreateView(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'artists/artist_form.html'
    success_url = reverse_lazy('artists:artist_list')

class ArtistUpdateView(UpdateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'artists/artist_form.html'
    success_url = reverse_lazy('artists:artist_list')

class ArtistDeleteView(DeleteView):
    model = Artist
    template_name = 'artists/artist_confirm_delete.html'
    success_url = reverse_lazy('artists:artist_list')


from django.shortcuts import render

# Create your views here.
