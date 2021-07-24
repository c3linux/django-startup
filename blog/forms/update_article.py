from django import forms
from django.forms import fields
from blog.models import ArticleModel


class updateArticleModelForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        exclude = ('writer', 'slug')
