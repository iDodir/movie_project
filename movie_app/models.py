from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUR = 'RUR'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (RUR, 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1_000_000)
    slug = models.SlugField(default='', null=False, db_index=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUR)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'
