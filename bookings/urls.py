from django.urls import path
from .views import (BookingListView,BookingDetailView,BookingCreateView,BookingUpdateView,BookingDeleteView,)

app_name = 'bookings'

urlpatterns = [
    path('', BookingListView.as_view(), name='booking_list'),
    path('add/', BookingCreateView.as_view(), name='booking_add'),
    path('<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('<int:pk>/edit/', BookingUpdateView.as_view(), name='booking_edit'),
    path('<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),
]