from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Goods(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название товара')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    image_1 = models.ImageField(upload_to='media/', default='media/None/no-img.jpg', verbose_name='Фото')
    image_2 = models.ImageField(upload_to='media/', default='media/None/no-img.jpg', verbose_name='Фото')
    image_3 = models.ImageField(upload_to='media/', default='media/None/no-img.jpg', verbose_name='Фото')
    image_4 = models.ImageField(upload_to='media/', default='media/None/no-img.jpg', verbose_name='Фото')
    image_5 = models.ImageField(upload_to='media/', default='media/None/no-img.jpg', verbose_name='Фото')
    image_6 = models.ImageField(upload_to='media/', default='media/None/no-img.jpg', verbose_name='Фото')
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='Категория')
    brand = models.CharField(max_length=50, verbose_name='Бренд')
    color = models.CharField(max_length=20, verbose_name='Цвет')
    size = models.CharField(max_length=20, verbose_name='Размер', null=True)
    quality = models.CharField(max_length=20, verbose_name='Состояние')
    status = models.BooleanField(verbose_name='Наличие товара', default=True)
    description = models.TextField(max_length=500, verbose_name='Описание', null=True)
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['name']


class Customer(models.Model):
    email = models.EmailField
    name = models.CharField(max_length=20, verbose_name='Имя')
    phone_number = PhoneNumberField(verbose_name='Мобильный номер')
    password = models.CharField(max_length=50, verbose_name='Пароль')
    country = models.CharField(max_length=90, verbose_name='Страна')
    city = models.CharField(max_length=189, verbose_name='Город')

    class Meta:
        verbose_name_plural = 'Покупатели'
        verbose_name = 'Покупатель'
        ordering = ['name']


class Order(models.Model):
    customer = models.ForeignKey('Customer', null=True, on_delete=models.PROTECT, verbose_name='Покупатель')
    good = models.ForeignKey('Goods', null=True, on_delete=models.PROTECT, verbose_name='Товар')
    order_status = models.CharField(max_length=20, verbose_name='Статус заказа')
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата')

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
