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
from articles.controllers import CommentsController, FavoriteController, CreateArticle, DetailsController

DEFAULT_COMMENTS_SHOWN = 10


class ArticleDetailView(View):

    def get(self, request, username, slug):
        comments_page = request.GET.get('page')
        comments_shown = request.GET.get('shown', DEFAULT_COMMENTS_SHOWN)

        context = DetailsController.create_detail_article(comments_shown=comments_shown,
                                                          username=username,
                                                          slug=slug,
                                                          comments_page=comments_page,
                                                          user=request.user)

        html = render(request, 'articles/detail.html', context)

        return HttpResponse(html)


class CommentsView(View):

    def post(self, request, slug=None):

        comment_form = CommentsController.create_new_comment(user=request.user,
                                                             slug=slug,
                                                             title=request.POST.get('title'),
                                                             text=request.POST.get('text'))
        article = get_object_or_404(Article, slug=slug)
        context = DetailsController.create_detail_article(username=article.author,
                                                          slug=slug,
                                                          user=request.user,
                                                          comment_form=comment_form)
        return HttpResponse(render(request, 'articles/detail.html', context))


class FavoriteView(View):

    def post(self, request, slug=None):

        FavoriteController.add_favorite(user=request.user, slug=slug)

        article = get_object_or_404(Article, slug=slug)
        context = DetailsController.create_detail_article(username=article.author,
                                                          slug=slug,
                                                          user=request.user)
        return HttpResponse(render(request, 'articles/detail.html', context))


class ResponseToView(View):

    def post(self, request, slug=None):
        article_form = CreateArticle.create_new_article(user=request.user,
                                                        values=request.POST,
                                                        slug=slug)
        article = get_object_or_404(Article, slug=slug)
        context = DetailsController.create_detail_article(username=article.author,
                                                          slug=slug,
                                                          user=request.user,
                                                          article_form=article_form)
        return HttpResponse(render(request, 'articles/detail.html', context))
