from django import forms
from django.urls import reverse_lazy
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView,)
from .models import Booking
from .forms import BookingForm,BookingUpdateForm


class BookingListView(ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'
    ordering = ['-event_date']

class BookingDetailView(DetailView):
    model = Booking
    template_name = 'bookings/booking_detail.html'
    context_object_name = 'booking'

class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('bookings:booking_list')

class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingUpdateForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('bookings:booking_list')

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'bookings/booking_confirm_delete.html'
    success_url = reverse_lazy('bookings:booking_list')


from django.shortcuts import render

# Create your views here.
