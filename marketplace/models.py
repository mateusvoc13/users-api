import json
import hashlib
from django.db import models


def idGenerator(data):
    hash = hashlib.md5(json.dumps(data, sort_keys=True).encode("utf-8")).hexdigest()
    return "%s-%s-%s-%s-%s" % (hash[:8], hash[8:12], hash[12:16], hash[16:20], hash[20:32])


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    productslist = models.ManyToManyField('Product', blank=True)

    def __str__(self):
        return "%s, %s" % (self.name, self.email)


class Product(models.Model):

    id = models.CharField(unique=True, primary_key=True, max_length=36)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=18, decimal_places=2)
    image = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    reviewScore = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return "%s, %s, %s" % (self.title, self.brand, self.price)
