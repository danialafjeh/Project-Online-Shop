from django.db import transaction
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product, Category, Brand, PharmacyInfo


def invalidate_main_cache(using):
    transaction.on_commit(
        lambda: cache.delete_pattern('main:*'),
        using=using
    )


@receiver(post_save, sender=Product)
@receiver(post_delete, sender=Product)
@receiver(post_save, sender=Category)
@receiver(post_delete, sender=Category)
@receiver(post_save, sender=Brand)
@receiver(post_delete, sender=Brand)
@receiver(post_save, sender=PharmacyInfo)
@receiver(post_delete, sender=PharmacyInfo)
def clear_main_cache(sender, instance, using, **kwargs):
    if kwargs.get('raw', False):
        return

    invalidate_main_cache(using)