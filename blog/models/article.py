from enum import unique
from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class ArticleModel(models.Model):
    image = models.ImageField(upload_to='article_images')
    title = models.CharField(max_length=50)
    body = RichTextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='body', unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name='article')
    writer = models.ForeignKey(
        'account.CustomUserModel', on_delete=models.CASCADE, related_name='articles')

    class Meta:
        db_table = 'article'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
