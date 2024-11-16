from django.db import models

from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=150, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Goods(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=5)
    description = models.TextField()
    buyer = models.ManyToManyField(Buyer, related_name='goods')

# Create your models here.
# Create your models here.
