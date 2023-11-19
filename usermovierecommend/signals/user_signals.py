from django.db.models.signals import post_save
from django.db.models.signals import post_delete
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


@receiver(post_delete, sender=User)
def before_user_deleted(sender, instance, **kwargs):
    elasticsearch_manager = ElasticsearchManager()
    es_instance = elasticsearch_manager.instance
    es = es_instance.es

    index_name = 'users'
    user_id = instance.id
    print(f"user id: {user_id}")
    query = {
        "query": {
            "match": {
                "id": user_id
            }
        }
    }
    try:
        response = es.delete_by_query(index=index_name,  body=query)
        print(f"response: {response}")
        if response['total'] != 0:
            if response['deleted'] == 1:
                print(f"Successfully deleted document from Elasticsearch. Document ID: {user_id}")
            else:
                raise Exception()
    except Exception as e:
        print(f"An error occurred while deleting the document in Elasticsearch: {e}")
        raise e
