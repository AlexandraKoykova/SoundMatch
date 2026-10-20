from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Booking(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        REJECTED = 'rejected', 'Rejected'

    class EventTypeChoices(models.TextChoices):
        WEDDING = 'wedding', 'Wedding'
        CLUB = 'club', 'Club'
        PRIVATE_PARTY = 'private_party', 'Private Party'
        CORPORATE = 'corporate', 'Corporate Event'
        OTHER = 'other', 'Other'

    artist = models.ForeignKey(
        'artists.Artist',
        on_delete=models.PROTECT,
        related_name='bookings',
    )
    client_name = models.CharField(
        max_length=100,
    )
    client_email = models.EmailField()
    client_phone = models.CharField(
        max_length=20,
    )
    event_date = models.DateField()
    event_location = models.CharField(
        max_length=150,
    )
    event_type = models.CharField(
        max_length=20,
        choices=EventTypeChoices.choices,
    )
    message = models.TextField(
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def clean(self):
        super().clean()

        if self.event_date and self.event_date < timezone.localdate():
            raise ValidationError({
                'event_date': 'The event date cannot be in the past.'
            })

        if (
                self.artist_id
                and self.event_date
                and self.status == self.StatusChoices.CONFIRMED
        ):
            conflicting_bookings = Booking.objects.filter(
                artist_id=self.artist_id,
                event_date=self.event_date,
                status=self.StatusChoices.CONFIRMED,
            ).exclude(pk=self.pk)

            if conflicting_bookings.exists():
                raise ValidationError({
                    'event_date': 'This artist is already booked for this date.'
                })

    def __str__(self):
        return f'{self.artist} - {self.event_date} ({self.status})'


from django.db import models

# Create your models here.
