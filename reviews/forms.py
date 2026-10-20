from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'artist',
            'reviewer_name',
            'rating',
            'comment',
        ]
        labels = {
            'artist': 'Artist',
            'reviewer_name': 'Your Name',
            'rating': 'Rating',
            'comment': 'Your Review',
        }
        widgets = {
            'reviewer_name': forms.TextInput(attrs={
                'placeholder': 'Enter your name',
            }),
            'rating': forms.Select(choices=[
                (1, '1 - Poor'),
                (2, '2 - Fair'),
                (3, '3 - Good'),
                (4, '4 - Very Good'),
                (5, '5 - Excellent'),
            ]),
            'comment': forms.Textarea(attrs={
                'placeholder': 'Share your experience',
                'rows': 4,
            }),
        }
        help_texts = {
            'rating': 'Choose a rating from 1 to 5.',
        }
    def clean_comment(self):
        comment = self.cleaned_data['comment'].strip()
        if len(comment) < 10:
            raise forms.ValidationError(
                'Your review must contain at least 10 characters.'
            )
        return comment