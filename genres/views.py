from django.urls import reverse_lazy
from django.views.generic import (ListView,DetailView,CreateView)
from .models import Genre
from .forms import GenreForm

class GenreListView(ListView):
    model = Genre
    template_name = 'genres/genre-list.html'
    context_object_name = 'genres'
    ordering = ['name']

class GenreDetailView(DetailView):
    model = Genre
    template_name = 'genres/genre-detail.html'
    context_object_name = 'genre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['artists'] = self.object.artists.all()

        return context

class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'genres/genre-form.html'
    success_url = reverse_lazy('genres:genre_list')


from django.shortcuts import render

# Create your views here.
