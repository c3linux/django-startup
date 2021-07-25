
from django.contrib.auth.decorators import login_required
from blog.models import CommentModel
from django.shortcuts import get_object_or_404, redirect


@login_required(login_url='/')
def delete_comment(request, id):
    comment = get_object_or_404(CommentModel, id=id)
    print("HEYY1")
    if comment.writer == request.user or comment.article.writer == request.user:
        print("HEYY")
        comment.delete()
        print("HELLO")
        return redirect('article', articleSlug=comment.article.slug)
    return redirect('homepage')
