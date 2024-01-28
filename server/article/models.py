from django.db import models
from django.utils import timezone

from user.models import User


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    body = models.CharField(max_length=10000)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)
    favourite_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(Article, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Article {self.title}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} liked {self.article.title}"
