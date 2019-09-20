from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category')
    slug = models.SlugField(max_length=100, verbose_name='Slug', unique=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)
