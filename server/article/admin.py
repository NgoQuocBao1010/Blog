from django.contrib import admin

from article.models import Article, Like

admin.site.register(Article)
admin.site.register(Like)
