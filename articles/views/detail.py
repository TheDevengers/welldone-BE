from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View

from articles.models import Article, Comment, Favorite
from articles.forms import CommentForm
from articles.controllers import CommentsController, FavoriteController
from users.models import Follower
from articles.forms import CommentForm, ArticleForm
from articles.controllers import CommentsController, FavoriteController, CreateArticle

DEFAULT_COMMENTS_SHOWN = 10


class ArticleDetailView(View):

    def get(self, request, username, slug):
        comments_page = request.GET.get('page')
        comments_shown = request.GET.get('shown', DEFAULT_COMMENTS_SHOWN)
        shown_param = '&shown={0}'.format(comments_shown) if comments_shown != DEFAULT_COMMENTS_SHOWN else ''
        article = get_object_or_404(Article.objects.select_related('author'), Q(slug=slug) & Q(publication_date__lte=datetime.now()) & Q(state__exact='PB'))

        if article.author.username == username:
            comments_list = Comment.objects.select_related('article').all().filter(article=article.pk).order_by('-creation_date')

            paginator = Paginator(comments_list, comments_shown)

            comments = paginator.get_page(comments_page)

            form = CommentForm()

            response = ArticleForm()

            is_followed = True if request.user.is_authenticated and Follower.objects.filter(follower=request.user, followed=article.author).exists() else False

            is_favorite = True if request.user.is_authenticated and Favorite.objects.filter(article=article, user=request.user).exists() else False

            context = {'article': article,
                       'username': username,
                       'comments': comments,
                       'shown_param': shown_param,
                       'form': form,
                       'is_favorite': is_favorite,
                       'response': response,
                       'is_followed': is_followed
                       }

            html = render(request, 'articles/detail.html', context)

            return HttpResponse(html)

        else:
            HttpResponse('')  # Show a Error Template


class CommentsView(View):
    def post(self, request, slug=None):
        CommentsController.create_new_comment(request=request, slug=slug)
        return redirect('article_detail', username=request.user, slug=slug)


class FavoriteView(View):
    def post(self, request, slug=None):
        FavoriteController.add_favorite(request=request, slug=slug)
        return redirect('article_detail', username=request.user, slug=slug)


class ResponseToView(View):
    def post(self, request, slug=None):
        CreateArticle.create_new_article(request=request, slug=slug)
        return redirect('article_detail', username=request.user, slug=slug)