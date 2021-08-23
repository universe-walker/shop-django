from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel, models.Model):
    name = models.CharField(_('название'), max_length=100)
    img = models.ImageField(_('путь к картинке'))
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='children',
        verbose_name=_('родительская категория')
    )

    class Meta:
        ordering = ['tree_id', 'lft']
        verbose_name = _('категория')
        verbose_name_plural = _('категории')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_('название товара'), max_length=140)
    description = models.TextField(_('описание'), max_length=255)
    price = models.IntegerField(_('цена'), validators=[MinValueValidator(0)])
    available = models.BooleanField(_('Доступен'), default=True)
    available_count = models.IntegerField(_('Доступное количество'), validators=[MinValueValidator(0)])
    slug = models.SlugField(max_length=140)
    rating = models.FloatField(_('Рейтинг'), validators=[MinValueValidator(0)])
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='категория'
    )

    class Meta:
        ordering = ['-price']
        verbose_name = _('товар')
        verbose_name_plural = _('товары')

    def __str__(self):
        return f'{self.name} категории: {self.category}'


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
