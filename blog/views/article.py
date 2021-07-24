from django.shortcuts import get_object_or_404, render
from blog.models import ArticleModel


def article(request, articleSlug):
    article = get_object_or_404(ArticleModel, slug=articleSlug)
    comments = article.comments.all()
    return render(request, 'pages/article.html', context={
        'article': article,
        'comments': comments
    })
