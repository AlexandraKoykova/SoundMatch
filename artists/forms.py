from django import forms
from .models import Artist


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = [
            'stage_name',
            'real_name',
            'bio',
            'city',
            'booking_price',
            'profile_image',
            'genres',
            'is_available',
        ]
        labels = {
            'stage_name': 'Stage Name',
            'real_name': 'Real Name',
            'bio': 'Biography',
            'city': 'City',
            'booking_price': 'Booking Price (€)',
            'profile_image': 'Profile Image',
            'genres': 'Music Genres',
            'is_available': 'Available for Bookings',
        }
        widgets = {
            'stage_name': forms.TextInput(attrs={
                'placeholder': 'Enter artist stage name',
            }),
            'real_name': forms.TextInput(attrs={
                'placeholder': 'Enter real name (optional)',
            }),
            'bio': forms.Textarea(attrs={
                'placeholder': 'Tell us about the artist',
                'rows': 4,
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'e.g. Sofia',
            }),
            'booking_price': forms.NumberInput(attrs={
                'placeholder': 'Enter booking price',
                'min': 0,
            }),
            'profile_image': forms.ClearableFileInput(),

            'genres': forms.CheckboxSelectMultiple(),
        }
        help_texts = {
            'booking_price': 'Enter the price in EUR.',
            'genres': 'Select one or more music genres.',
        }
    def clean_booking_price(self):
        price = self.cleaned_data['booking_price']

        if price <= 0:
            raise forms.ValidationError(
                'Booking price must be greater than zero.'
            )
        return price