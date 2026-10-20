from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField(
        blank=True,
    )
    def __str__(self):
        return self.name


from django.db import models

# Create your models here.
