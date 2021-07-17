
from django.contrib import admin
from blog.models import (CategoryModel, ArticleModel,
                         CommentModel, ContactModel)
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


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_time')
    search_fields = ('email',)


admin.site.register(ContactModel, ContactAdmin)
