from django.db import models
from django.contrib.auth.models import User
from blog.models import ArticleModel, article
from blog.abstract_models import DateAbstractModel


class CommentModel(DateAbstractModel):
    writer = models.ForeignKey(
        'account.CustomUserModel', on_delete=models.CASCADE, related_name='comment')
    article = models.ForeignKey(
        ArticleModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    class Meta:
        db_table = 'comment'
        verbose_name = 'comment'
        verbose_name_plural = 'comment'

    def __str__(self):
        return 'Comment'
