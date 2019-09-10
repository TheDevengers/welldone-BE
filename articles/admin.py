from django.contrib import admin
from articles.models import Article, Category, Comment, Highlight

admin.site.site_header = "Welldone admin"
admin.site.site_title = "Welldone admin portal"
admin.site.index_title = "Welcome to Welldone admin Portal"


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Highlight)
