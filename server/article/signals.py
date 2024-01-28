from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from article.models import Article, Like

@receiver(post_save, sender=Like)
def like_created(sender, instance, created, **kwargs):
    if created:
        instance.article.favourite_count += 1
        instance.article.save()
        

@receiver(pre_delete, sender=Like)
def like_deleted(sender, instance, **kwargs):
    instance.article.favourite_count -= 1
    instance.article.save()