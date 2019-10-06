from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    productslist = models.ManyToManyField('Product', blank=True)

    def __str__(self):
        return "%s, %s" % (self.name, self.email)


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=18, decimal_places=2)
    image = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    reviewscore = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return "%s, %s, %s" % (self.title, self.brand, self.price)
