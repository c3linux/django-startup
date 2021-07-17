
from django.contrib import admin
from blog.models import (CategoryModel, ArticleModel,
                         CommentModel, ContactModel)
# Register your models here.
admin.site.register(CategoryModel)


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'body')
    list_display = (
        'title', 'body', 'created_time', 'updated_time'
    )


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('writer', 'created_time', 'updated_time')
    search_fields = ('writer__username',)


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_time')
    search_fields = ('email',)
