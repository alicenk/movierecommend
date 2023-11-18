from django.db.models.signals import post_save
from django.dispatch import receiver
from usermovierecommend.models.user import User


@receiver(post_save, sender=User)
def after_user_creation(sender, instance, created, **kwargs):
    if created:
        print(f"Yeni kullanıcı eklendi: {instance.name}")
        # İşlemlerinizi burada gerçekleştirin.
