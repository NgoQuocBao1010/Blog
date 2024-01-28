from django.urls import path, include
from rest_framework import routers

from article.views import ListAddArticleView, ArticleDetailView, FavoriteArticleView


urlpatterns = [
    path("api/articles/", ListAddArticleView.as_view(), name="all_articles"),
    path(
        "api/articles/<int:pk>/",
        ArticleDetailView.as_view(),
        name="shopping_list_detail",
    ),
    path(
        "api/articles/<int:pk>/favorite",
        FavoriteArticleView.as_view(),
        name="favorite_articles",
    ),
]
