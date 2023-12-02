from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
from usermovierecommend.models.usermovie import UserMovie
from usermovierecommend.elasticsearch.documents import UserMovieDocument
from elasticsearch import Elasticsearch
from usermovierecommend.elasticsearch.elasticsearch_manager import ElasticsearchManager


@receiver(post_save, sender=UserMovie)
def after_usermovie_creation(sender, instance, created, **kwargs):
    if created:
        elasticsearch_manager = ElasticsearchManager()
        es_instance = elasticsearch_manager.instance
        es = es_instance.es

        usermovie_document = UserMovieDocument()
        response = es.index(index=usermovie_document.index, body=usermovie_document.document(instance))

        if response['result'] == 'created':
            print(f"Document Created Successfully Document ID: {response['_id']}")
        else:
            print("An error occurred while uploading the document.")
    else:
        print(f"Model updated: {instance.name}")


@receiver(post_delete, sender=UserMovie)
def after_usermovie_deleted(sender, instance, **kwargs):
    elasticsearch_manager = ElasticsearchManager()
    es_instance = elasticsearch_manager.instance
    es = es_instance.es

    index_name = 'usermovies'
    usermovie_id = instance.id

    query = {
        "query": {
            "match": {
                "id": usermovie_id
            }
        }
    }
    try:
        response = es.delete_by_query(index=index_name,  body=query)
        print(f"response: {response}")
        if response['total'] != 0:
            if response['deleted'] == 1:
                print(f"Successfully deleted document from Elasticsearch. Document ID: {usermovie_id}")
            else:
                raise Exception()
    except Exception as e:
        print(f"An error occurred while deleting the document in Elasticsearch: {e}")
        raise e
