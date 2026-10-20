from django.db import models


class Artist(models.Model):
    stage_name = models.CharField(
        max_length=100,
        unique=True,
    )
    real_name = models.CharField(
        max_length=100,
        blank=True,
    )
    bio = models.TextField()
    city = models.CharField(
        max_length=100,
    )
    booking_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    profile_image = models.URLField(
        blank=True,
    )
    genres = models.ManyToManyField(
        'genres.Genre',
        related_name='artists',
    )
    is_available = models.BooleanField(
        default=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.stage_name


from django.db import models

# Create your models here.
