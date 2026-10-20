from django import forms

from .models import Genre


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre

        fields = [
            'name',
            'description',
        ]
        labels = {
            'name': 'Genre Name',
            'description': 'Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. Pop, Rock, Jazz',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe this music genre',
                'rows': 3,
            }),
        }
        help_texts = {
            'name': 'Enter a music genre name.',
            'description': 'Optional description.',
        }
    def clean_name(self):
        name = self.cleaned_data['name'].strip()

        existing_genres = Genre.objects.filter(
            name__iexact=name
        )
        if self.instance.pk:
            existing_genres = existing_genres.exclude(
                pk=self.instance.pk
            )
        if existing_genres.exists():
            raise forms.ValidationError(
                'This music genre already exists.'
            )
        return name