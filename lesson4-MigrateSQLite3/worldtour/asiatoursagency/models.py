from django.db import models

# Create your models here.
class Tour(models.Model):
    # we need a origin country, we need a destination, number of nights, and we need the price for that tour.
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()


    
    
    