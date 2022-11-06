from django.db import models
from django.contrib.auth import get_user_model 
from django.urls import reverse


from slugify import slugify
from .utils import get_time


User = get_user_model()


class Lost(models.Model):
    CATEGORY_CHOICES = (
        ('documents', 'Документ'),
        ('keys', 'Ключи'),
        ('technique', 'Техника'),
        ('wallets', 'Кошельки'),
        ('animals', 'Животные'),
        ('decorations', 'Украшения'),
        ('bags', 'Сумки'),
        ('other', 'Другое')
    )

    STATUS_CHOICES = (
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('draft', 'Draft')
    )
    ADDRESS_CHOICES = (
        ('XXXXXX', 'xxxxxx'),
        ('YYYYYY', 'yyyyyy')
    )

    user = models.ForeignKey(
        verbose_name='Автор поста',
        to=User,
        on_delete=models.CASCADE,
        related_name='publications'
    )
    title = models.CharField(verbose_name='Что потеряли?', max_length=200)
    slug = models.SlugField(max_length=170, primary_key=True, blank=True)
    image = models.ImageField(upload_to='post_images')
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='draft'
    )
    text = models.TextField()
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default=False
    )
    address = models.CharField(max_length=100, choices=ADDRESS_CHOICES)
    date = models.DateField(verbose_name='Дата потерии')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + get_time())
        super().save(*args, **kwargs)

    
    class Meta:
        ordering = ('created_at', )

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


class LostImage(models.Model):
    image = models.ImageField(upload_to='post_images/carousel')
    post = models.ForeignKey(
        to=Lost,
        on_delete=models.CASCADE,
        related_name='post_images'
    )










