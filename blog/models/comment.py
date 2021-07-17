from django.db import models
from django.contrib.auth.models import User
from blog.models import ArticleModel, article


class CommentModel(models.Model):
    writer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment')
    article = models.ForeignKey(
        ArticleModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'
        verbose_name = 'comment'
        verbose_name_plural = 'comment'

    def __str__(self):
        return 'Comment'
