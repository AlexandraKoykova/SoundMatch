from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    artist = models.ForeignKey(
        'artists.Artist',
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    reviewer_name = models.CharField(
        max_length=100,
    )
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    def __str__(self):
        return f'{self.reviewer_name} - {self.artist} ({self.rating}/5)'


from django.db import models

# Create your models here.
