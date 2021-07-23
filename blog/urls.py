
from django.urls import path
from blog.views import contact, homepage, category, my_articles

urlpatterns = [
    path('', homepage, name='homepage'),
    path('contact/', contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('my-articles', my_articles, name='my_articles')
]
