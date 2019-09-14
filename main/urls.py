"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from articles.views.views import ArticleDetailView
from articles.views.lists import LatestArticlesView
from users.views.views import user_articles

from users.api.api import UsersAPI, UserAPI
from articles.api.api import ArticlesAPI, ArticleAPI, CategoriesAPI

api_path = 'api/v1'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('author/<str:username>', user_articles, name='user_articles'),

    path('article/<str:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('', LatestArticlesView.as_view(), name='latest_articles'),

# API
    # TODO Rewrite them depends on your necessities, but notify to the team
    # TODO Comments at the end of line are explicative. Consider remove it if you want
    #path('{0}/articles/<int:pk>/comments'.format(api_path), view, name='article_comments_api'),  # GET, POST
    #path('{0}/articles/<int:pk>/favorites'.format(api_path), view, name='article_favorite_api'),  # POST, DELETE
    #path('{0}/articles/<int:pk>/highlights/<int:pk>'.format(api_path), view, name='article_highlight_api'),  # DELETE
    #path('{0}/articles/<int:pk>/highlights'.format(api_path), view, name='article_highlights_api'),  # POST
    # FIXME next endpoint send a mention notification, not list mentions
    #path('{0}/articles/<int:pk>/mention'.format(api_path), view, name='article_mention_api'),
    path('{0}/articles/<int:pk>'.format(api_path), ArticleAPI.as_view(), name='article_api'),  # PUT, DELETE
    path('{0}/articles'.format(api_path), ArticlesAPI.as_view(), name='articles_api'),  # GET, POST

    #path('{0}/users/<int:pk>/highlights'.format(api_path), view, name='user_highlights_api'),  # GET
    #path('{0}/users/<int:pk>/follow'.format(api_path), view, name='user_follow_api'),
    #path('{0}/users/<int:pk>/unfollow'.format(api_path), view, name='user_unfollow_api'),
    path('{0}/users/<int:pk>'.format(api_path), UserAPI.as_view(), name='user_api'),  # PUT, DELETE
    path('{0}/users'.format(api_path), UsersAPI.as_view(), name='users_api'),  # GET, POST

    #Categories
    path('{0}/categories'.format(api_path), CategoriesAPI.as_view(), name='categories_api'),  # GET,

]
