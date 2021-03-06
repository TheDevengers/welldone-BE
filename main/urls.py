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
from rest_framework_simplejwt import views as jwt_views

from users.views import Signup, Logout, Login, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView, FollowView, UnfollowView, MyTokenObtainPairView
from articles.api import ArticleAPI, ArticlesAPI, CategoriesAPI, FavoritesAPI
from articles.views import LatestArticlesView, ArticleDetailView, AuthorArticlesView, CategoryArticlesView, \
    CommentsView, FavoriteView, ResponseToView, CategoriesListView, UserListView
from users.api import UserAPI, UsersAPI

api_path = 'api/v1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/signup', Signup.as_view(), name='signup_web'),
    path('user/logout', Logout.as_view(), name='logout_web'),
    path('user/login', Login.as_view(), name='login_web'),
    path(r'password_reset', PasswordResetView.as_view(), name='password_reset_url'),
    path(r'password_reset_done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path(r'password_reset_confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path(r'password_reset_complete', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('authors/', UserListView.as_view(), name='users_list'),
    path('author/<str:username>', AuthorArticlesView.as_view(), name='user_articles'),
    path('categories/', CategoriesListView.as_view(), name='categories_list'),
    path('category/<str:slug>', CategoryArticlesView.as_view(), name='category_articles'),

    path('<str:username>/<str:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('comments/<str:slug>', CommentsView.as_view(), name='article_comments'),
    path('favorite/<str:slug>', FavoriteView.as_view(), name='article_favorites'),
    path('follow/<str:username>', FollowView.as_view(), name='user_follow'),
    path('unfollow/<str:username>', UnfollowView.as_view(), name='user_unfollow'),
    path('response_to/<str:slug>', ResponseToView.as_view(), name='article_response_to'),
    path('', LatestArticlesView.as_view(), name='latest_articles'),

    # API
    #path('{0}/token/'.format(api_path), jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('{0}/token/'.format(api_path), MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('{0}/token/refresh/'.format(api_path), jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
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
    path('{0}/users/<int:pk>'.format(api_path), UserAPI.as_view(), name='user_api'),  # GET, PUT, DELETE
    path('{0}/users'.format(api_path), UsersAPI.as_view(), name='users_api'),  # GET, POST

    path('{0}/categories'.format(api_path), CategoriesAPI.as_view(), name='categories_api'),  # GET,
    path('{0}/favorites'.format(api_path), FavoritesAPI.as_view(), name='favorite_api')

]

handler400 = 'articles.views.error_400'
handler403 = 'articles.views.error_403'
handler404 = 'articles.views.error_404'
handler500 = 'articles.views.error_500'
