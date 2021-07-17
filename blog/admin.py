
from django.contrib import admin
from blog.models import (CategoryModel, ArticleModel, CommentModel)
# Register your models here.
admin.site.register(CategoryModel)


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'body')
    list_display = (
        'title', 'body', 'created_time', 'updated_time'
    )


admin.site.register(ArticleModel, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('writer', 'created_time', 'updated_time')
    search_fields = ('writer__username',)


admin.site.register(CommentModel, CommentAdmin)
