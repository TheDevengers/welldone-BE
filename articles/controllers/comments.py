from django.shortcuts import get_object_or_404

from articles.models import Article, Comment
from articles.forms import CommentForm


class CommentsController(object):

    @staticmethod
    def create_new_comment(request, slug):
        comment = Comment()
        comment.author = request.user
        article = get_object_or_404(Article, slug=slug)
        comment.article = article
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()