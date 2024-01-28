from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from article.api.serializers import (
    ArticleSerializer,
    ArticleCreateUpdateSerializer,
    ArticleWithLikesSerializer,
)
from article.models import Article, Like


class ListAddArticleView(generics.ListCreateAPIView):
    queryset = Article.objects.all().order_by("-created_at")
    permission_classes = [AllowAny]
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ArticleCreateUpdateSerializer

        # If "GET"
        return ArticleSerializer

    def create(self, request, *args, **kwargs):
        # Instantiate the serializer
        serializer = self.get_serializer(data=request.data)

        # Perform validation and respond with error messages if failed
        serializer.is_valid(raise_exception=True)

        # Create a new instance
        self.perform_create(serializer)

        # Return the serialized data
        return Response(
            ArticleSerializer(serializer.instance).data, status=status.HTTP_201_CREATED
        )


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return ArticleCreateUpdateSerializer

        # If "GET"
        return ArticleWithLikesSerializer

    def put(self, request, *args, **kwargs):
        # Check whether this update is partial (partial=PATCH)
        partial = kwargs.pop("partial", False)

        # Get the model instance
        instance = self.get_object()

        # Instantiate the serializer and pass the `partial` arg to it
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        # Perform validation and respond with error messages if failed
        serializer.is_valid(raise_exception=True)

        # Check if there are any changes between the new data and the existing instance
        if not any(
            serializer.validated_data.get(field) != getattr(instance, field)
            for field in serializer.validated_data.keys()
        ):
            # If no changes detected, return a No Content response
            return Response(
                {"message": "No changes detected."},
                status=status.HTTP_204_NO_CONTENT,
            )

        # Update the instance
        self.perform_update(serializer)

        # Return the serialized data
        return Response(ArticleSerializer(instance).data)

    def delete(self, request, *args, **kwargs):
        # Get the model instance
        instance = self.get_object()

        # Simply delete - no need to instantiate the serializer
        self.perform_destroy(instance)

        return Response(
            {"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class FavoriteArticleView(generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Get the model instance
        article = self.get_object()

        # Auth user
        user = request.user

        existing_like = Like.objects.filter(user=user, article=article).first()
        if existing_like:
            return Response(
                {"detail": "You have already liked this article."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create a new like
        like = Like(user=user, article=article)
        like.save()

        return Response(ArticleSerializer(article).data)

    def delete(self, request, *args, **kwargs):
        # Get the model instance
        article = self.get_object()

        # Auth user
        user = request.user

        like = Like.objects.filter(user=user, article=article).first()

        if not like:
            return Response(
                {"detail": "You have not liked this article."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Delete the like instance
        like.delete()

        return Response(ArticleSerializer(self.get_object()).data)
