from django.db import models

class MoviesData(models.Model):
    name = models.CharField(max_length=150)
    rating = models.FloatField()

    def __str__(self):
        return self.name