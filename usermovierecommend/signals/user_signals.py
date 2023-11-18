from django.db.models.signals import post_save
from django.dispatch import receiver
from usermovierecommend.models.user import User
from usermovierecommend.elasticsearch.documents import UserDocument


@receiver(post_save, sender=User)
def after_user_creation(sender, instance, created, **kwargs):
    if created:
        print(f"After Save User: {instance.name}")

        user_document = UserDocument(
            meta={'id': instance.id},
            name=instance.name,
            surname=instance.surname,
            email=instance.email,
        )

        print(f"New User user_document: {user_document}")
        ## user_document.save() save aşamasında hata alıyorum, çözünce devreye alıcam.
    else:
        print(f"Model updated: {instance.name}")
