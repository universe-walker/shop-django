from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify


class Category(MPTTModel, models.Model):
    name = models.CharField(_('название'), max_length=100)
    img = models.ImageField(_('путь к картинке'), blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='children',
        related_query_name='child',
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('category_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse_lazy('category_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse_lazy('category_delete', kwargs={'slug': self.slug})


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
        related_query_name='product',
        verbose_name='категория'
    )

    class Meta:
        ordering = ['-price']
        verbose_name = _('товар')
        verbose_name_plural = _('товары')

    def __str__(self):
        return f'{self.name} категории: {self.category}'


class Characteristic(models.Model):
    name = models.CharField(_('характеристика'), max_length=100)
    value = models.CharField(_('значение'), max_length=100)
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='characteristics',
        related_query_name='characteristic',
        verbose_name=_('товар')
    )

    class Meta:
        ordering = ['name']
        verbose_name = _('характеристика')
        verbose_name_plural = _('характеристик')

    def __str__(self):
        return f'{self.name} - {self.value}'


class ProductImage(models.Model):
    path = models.ImageField(_('путь'))
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('товар')
    )

    class Meta:
        verbose_name = _('картинка товара')
        verbose_name_plural = _('картинки товаров')

    def __str__(self):
        return f'Картинка товара {self.product}'


class Discount(models.Model):
    percent = models.PositiveSmallIntegerField(verbose_name=_('процент скидки'), validators=[MaxValueValidator(100)])
    start_datetime = models.DateTimeField(verbose_name=_('время начала скидки'))
    end_datetime = models.DateTimeField(verbose_name=_('время конца скидки'))
    products = models.ManyToManyField(
        'Product',
        related_name='discounts',
        related_query_name='discount',
        verbose_name=_('скидка')
    )

    class Meta:
        ordering = ['percent']
        verbose_name = _('скидка')
        verbose_name_plural = _('скидки')
