from blog.forms.update_article import updateArticleModelForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls.conf import path
from blog.forms import addArticleModelForm
from blog.models import ArticleModel


@login_required(login_url='/')
def update_article(request, updateArticleSlug):
    article = get_object_or_404(
        ArticleModel, slug=updateArticleSlug, writer=request.user)
    form = updateArticleModelForm(
        request.POST or None, files=request.FILES or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('article', articleSlug=article.slug)
    return render(request, 'pages/update-article.html', context={
        'form': form
    })
