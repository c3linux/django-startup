from blog.models.article import ArticleModel
from django.contrib import admin
from blog.models import CategoryModel
# Register your models here.
admin.site.register(CategoryModel)


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'body')
    list_display = (
        'title', 'body', 'created_time', 'updated_time'
    )


admin.site.register(ArticleModel, ArticleAdmin)
