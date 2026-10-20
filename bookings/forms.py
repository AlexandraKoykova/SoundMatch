from django import forms
from django.utils import timezone

from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'artist',
            'client_name',
            'client_email',
            'client_phone',
            'event_date',
            'event_location',
            'event_type',
            'message',
        ]
        labels = {
            'artist': 'Choose Artist',
            'client_name': 'Your Name',
            'client_email': 'Email Address',
            'client_phone': 'Phone Number',
            'event_date': 'Event Date',
            'event_location': 'Event Location',
            'event_type': 'Event Type',
            'message': 'Additional Information',
        }
        widgets = {
            'client_name': forms.TextInput(attrs={
                'placeholder': 'Enter your full name',
            }),
            'client_email': forms.EmailInput(attrs={
                'placeholder': 'example@email.com',
            }),
            'client_phone': forms.TextInput(attrs={
                'placeholder': '+359...',
            }),
            'event_date': forms.DateInput(attrs={
                'type': 'date',
            }),
            'event_location': forms.TextInput(attrs={
                'placeholder': 'e.g. Sofia',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Tell us about your event',
                'rows': 4,
            }),
        }
        help_texts = {
            'event_date': 'Choose a future date.',
            'message': 'Optional details about your event.',
        }

    def clean_event_date(self):
        event_date = self.cleaned_data['event_date']

        if event_date < timezone.localdate():
            raise forms.ValidationError(
                'The event date cannot be in the past.'
            )

        return event_date

class BookingUpdateForm(BookingForm):
    class Meta(BookingForm.Meta):
        fields = BookingForm.Meta.fields + ['status']
        widgets = {
            **BookingForm.Meta.widgets,
            'client_name': forms.TextInput(attrs={'readonly': True}),
        }
