from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404

from articles.forms import CommentForm, ArticleForm
from articles.models import Article, Comment, Favorite
from users.models import Follower

DEFAULT_COMMENTS_SHOWN = 10

class DetailsController(object):

    @staticmethod
    def create_detail_article(username, slug, user, comment_form=None, article_form=None,
                              comments_shown=10, comments_page=1):

        shown_param = '&shown={0}'.format(comments_shown) if comments_shown != DEFAULT_COMMENTS_SHOWN else ''
        article = get_object_or_404(Article.objects.select_related('author'),
                                    Q(author__username=username) & Q(slug=slug) & Q(
                                        publication_date__lte=datetime.now()) & Q(state__exact='PB'))
        comments_list = Comment.objects.select_related('article').all().filter(article=article.pk).order_by(
            '-creation_date')
        paginator = Paginator(comments_list, comments_shown)
        comments = paginator.get_page(comments_page)
        form = CommentForm() if comment_form is None else comment_form
        reply = ArticleForm() if article_form is None else article_form
        is_followed = True if user.is_authenticated and Follower.objects.filter(follower=user,
                                                                                followed=article.author).exists() else False
        is_favorite = True if user.is_authenticated and Favorite.objects.filter(article=article,
                                                                                user=user).exists() else False

        context = {'article': article,
                   'username': username,
                   'comments': comments,
                   'shown_param': shown_param,
                   'form': form,
                   'is_favorite': is_favorite,
                   'response': reply,
                   'is_followed': is_followed
                   }
        return context
