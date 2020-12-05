from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.CharField(max_length=10)
    places_to_purchase = models.CharField(max_length=50)
    lowest_price = models.DecimalField(max_digits = 8, decimal_places=2)

    class Meta:
        verbose_name_plural = "books"

    def __str__(self):
        return self.title
