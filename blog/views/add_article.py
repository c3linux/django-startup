from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls.conf import path
from blog.forms import addArticleModelForm


@login_required(login_url='/')
def add_article(request):
    form = addArticleModelForm(
        request.POST or None, files=request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.writer = request.user
        article.save()
        form.save_m2m()
        return redirect('article', articleSlug=article.slug)
    return render(request, 'pages/add-article.html', context={
        'form': form
    })
