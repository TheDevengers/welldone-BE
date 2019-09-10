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

api_path = 'api/v1'

urlpatterns = [
    path('admin/', admin.site.urls),

    # API
    path('{0}/articles/<int:pk>/comments'.format(api_path), view, name='article_comments_api'),
    path('{0}/articles/<int:pk>/favorite'.format(api_path), view, name='article_favorite_api'),
    path('{0}/articles/<int:pk>/highlight/<int:pk>'.format(api_path), view, name='article_highlight_api'),
    path('{0}/articles/<int:pk>/highlight'.format(api_path), view, name='article_highlights_api'),
    path('{0}/articles/<int:pk>/mention'.format(api_path), view, name='article_mention_api'),
    path('{0}/articles/<int:pk>'.format(api_path), view, name='article_api'),
    path('{0}/articles'.format(api_path), view, name='articles_api'),

    path('{0}/users/<int:pk>/follow'.format(api_path), view, name='user_follow_api'),
    path('{0}/users/<int:pk>/unfollow'.format(api_path), view, name='user_unfollow_api'),
    path('{0}/users/<int:pk>'.format(api_path), view, name='user_api'),
    path('{0}/users'.format(api_path), view, name='users_api'),
]
