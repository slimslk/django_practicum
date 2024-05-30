from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    profile = models.URLField(max_length=255, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    rating = models.FloatField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
