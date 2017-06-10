# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 02:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='Название товара')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='Количество')),
                ('unit', models.CharField(choices=[('кг', 'Килограммы'), ('г', 'Граммы'), ('л', 'Литры')], default='кг', max_length=16, verbose_name='Единица измерения')),
                ('category', models.CharField(choices=[('овощи', 'Овощи'), ('фрукты', 'Фрукты'), ('рыба', 'Рыба'), ('мясо', 'Мясо'), ('напитки', 'Напитки'), ('алкоголь', 'Алкоголь')], default='мясо', max_length=64, verbose_name='Категория товара')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Стартовая цена')),
                ('percentage', models.PositiveSmallIntegerField(default=100, verbose_name='Скидка/Наценка')),
                ('img', models.ImageField(null=True, upload_to=product.models.get_product_image, verbose_name='Изображение товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='WishlistTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата транзакции')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='transaction',
            field=models.ManyToManyField(through='product.WishlistTransaction', to=settings.AUTH_USER_MODEL),
        ),
    ]