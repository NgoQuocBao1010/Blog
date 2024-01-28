from rest_framework import serializers

from article.models import Article, Like


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ("id",)


# Serializer for POST and PUT requests
class ArticleCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "body")


class ArticleWithLikesSerializer(serializers.ModelSerializer):
    likeBy = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = "__all__"

    def get_likeBy(self, obj):
        likes = Like.objects.filter(article=obj)
        return [like.user.email for like in likes]
