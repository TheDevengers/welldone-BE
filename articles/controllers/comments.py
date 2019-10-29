from django.shortcuts import get_object_or_404

from articles.models import Article, Comment
from articles.forms import CommentForm


class CommentsController(object):

    @staticmethod
    def create_new_comment(user, slug, title, text):
        comment = Comment()
        comment.author = user
        article = get_object_or_404(Article, slug=slug)
        comment.article = article
        form_data = dict(
            title=title,
            text=text
        )
        form = CommentForm(form_data, instance=comment)
        if form.is_valid():
            form.save()
            return None
        return form