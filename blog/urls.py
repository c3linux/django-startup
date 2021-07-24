

from django.urls import path
from blog.views import contact, homepage, category, my_articles, article, add_article, update_article, delete_article

urlpatterns = [
    path('', homepage, name='homepage'),
    path('contact/', contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('my-articles', my_articles, name='my_articles'),
    path('article/<slug:articleSlug>', article, name='article'),
    path('add-article', add_article, name='add-article'),
    path('update-article/<slug:updateArticleSlug>',
         update_article, name='update-article'),
    path('delete-article/<slug:deleteArticleSlug>',
         delete_article, name='delete-article'),
]
