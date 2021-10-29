from django.db import models

class Offer(models.Model):
    name = models.CharField("Name", max_length=100)
    price = models.FloatField("Price", default=0.0)

    