from django.conf import settings
from django.db import models
import os, uuid

def get_product_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{0}.{1}".format(uuid.uuid4(), ext)
    return os.path.join('goods', filename)

class Product(models.Model):
    UNIT_CHOICES = (
        ('кг', 'Килограммы'),
        ('г', 'Граммы'),
        ('л', 'Литры')
    )
    CATEGORY_CHOICES = (
        ('овощи', 'Овощи'),
        ('фрукты', 'Фрукты'),
        ('рыба', 'Рыба'),
        ('мясо', 'Мясо'),
        ('напитки', 'Напитки'),
        ('алкоголь', 'Алкоголь'),
    )
    name = models.CharField(
        db_index=True,
        max_length=64,
        unique=True,
        verbose_name='Название товара'
    )
    quantity = models.PositiveSmallIntegerField(
        default=1, verbose_name='Количество')
    unit = models.CharField(
        choices=UNIT_CHOICES,
        default='кг',
        max_length=16,
        verbose_name='Единица измерения'
    )
    category = models.CharField(
        choices=CATEGORY_CHOICES,
        default='мясо',
        max_length=64,
        verbose_name='Категория товара'
    )
    price = models.PositiveIntegerField(
        default=0, verbose_name='Стартовая цена')
    percentage = models.PositiveSmallIntegerField(
        default=100, verbose_name='Скидка/Наценка')
    img = models.ImageField(
        upload_to=get_product_image, verbose_name='Изображение товара', null=True)

    transaction = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='WishlistTransaction'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class WishlistTransaction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата транзакции'
    )
