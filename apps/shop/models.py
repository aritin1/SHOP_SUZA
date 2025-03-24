from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=25,
        verbose_name="Название категории"
    )
    description = models.TextField(
        verbose_name="Описание категории",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Brand(models.Model):
    name = models.CharField(
        max_length=25,
    )
    description = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Product(models.Model):
    class GenderChoices(models.TextChoices):
        MEN = "M", "Мужчины"
        WOMEN = "F", "Женщины"

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=1,
        choices=GenderChoices.choices,
        default=GenderChoices.MEN
    )
    name = models.CharField(
        max_length=25,
        verbose_name="Название продукта"
    )
    count = models.IntegerField(
        default=0,
        verbose_name="Количество"
    )
    price = models.FloatField(
        default=0,
        verbose_name="Цена"
    )
    created_at = models.DateField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='products/'
    )
