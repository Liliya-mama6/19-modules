from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(decimal_places=80, max_digits=99)
    age = models.IntegerField()


class Game(models.Model):
    title = models.CharField(max_length=40)
    cost = models.DecimalField(decimal_places=80, max_digits=99)
    size = models.DecimalField(decimal_places=80, max_digits=99)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')
