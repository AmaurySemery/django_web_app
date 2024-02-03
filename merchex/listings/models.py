from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    # Afficher le nom des entrées dans le panneau d'admin
    def __str__(self):
        return f'{self.name}'

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=50)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

class Listing(models.Model):
   band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)