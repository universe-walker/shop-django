from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField()
    slug = models.SlugField(max_length=100)
    parent = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='children'
    )


class Product(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    available = models.BooleanField(default=True)
    available_count = models.IntegerField(validators=[MinValueValidator(0)])
    slug = models.SlugField(max_length=140)
    rating = models.FloatField(validators=[MinValueValidator(0)])
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='products'
    )


class Characteristic(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='characteristics'
    )


class ProductImage(models.Model):
    path = models.ImageField()
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='images'
    )


class Discount(models.Model):
    percent = models.PositiveSmallIntegerField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    products = models.ManyToManyField(
        'Product',
        related_name='discounts'
    )
