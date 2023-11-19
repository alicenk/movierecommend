from django.db.models.signals import post_save
from django.dispatch import receiver
from usermovierecommend.models.user import User
from usermovierecommend.elasticsearch.documents import UserDocument
from elasticsearch import Elasticsearch
from usermovierecommend.elasticsearch.elasticsearch_manager import ElasticsearchManager


@receiver(post_save, sender=User)
def after_user_creation(sender, instance, created, **kwargs):
    if created:
        elasticsearch_manager = ElasticsearchManager()
        es_instance = elasticsearch_manager.instance
        es = es_instance.es

        user_document = UserDocument()
        response = es.index(index=user_document.index, body=user_document.document(instance))

        if response['result'] == 'created':
            print(f"Document Created Successfully Document ID: {response['_id']}")
        else:
            print("An error occurred while uploading the document.")
    else:
        print(f"Model updated: {instance.name}")
