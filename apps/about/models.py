from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    email = models.EmailField(
        verbose_name='E-mail'
    )
    phone = PhoneNumberField()
    instagram = models.URLField(
        verbose_name='Instagram',
        null=True,
        blank=True
    )
    address = models.URLField(
        verbose_name='Address',
        null=True,
        blank=True
    )
    facebook = models.URLField(
        verbose_name='Facebook',
        null=True,
        blank=True
    )
    twitter = models.URLField(
        verbose_name='Twitter',
        null=True,
        blank=True
    )
    linkedin = models.URLField(
        verbose_name='Linkedin',
        null=True,
        blank=True
    )
    github = models.URLField(
        verbose_name='Github',
        null=True,
        blank=True
    )
    tiktok = models.URLField(
        verbose_name='TikTok',
        null=True,
        blank=True
    )



class AboutUs(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=100
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    image = models.ImageField(
        verbose_name='Image',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title