from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
from usermovierecommend.models.movie import Movie
from usermovierecommend.elasticsearch.documents import MovieDocument
from elasticsearch import Elasticsearch
from usermovierecommend.elasticsearch.elasticsearch_manager import ElasticsearchManager


@receiver(post_save, sender=Movie)
def after_movie_creation(sender, instance, created, **kwargs):
    if created:
        elasticsearch_manager = ElasticsearchManager()
        es_instance = elasticsearch_manager.instance
        es = es_instance.es

        movie_document = MovieDocument()
        response = es.index(index=movie_document.index, body=movie_document.document(instance))

        if response['result'] == 'created':
            print(f"Document Created Successfully Document ID: {response['_id']}")
        else:
            print("An error occurred while uploading the document.")
    else:
        print(f"Model updated: {instance.name}")


@receiver(post_delete, sender=Movie)
def before_movie_deleted(sender, instance, **kwargs):
    elasticsearch_manager = ElasticsearchManager()
    es_instance = elasticsearch_manager.instance
    es = es_instance.es

    index_name = 'movies'
    movie_id = instance.id
    print(f"movie id: {movie_id}")
    query = {
        "query": {
            "match": {
                "id": movie_id
            }
        }
    }
    try:
        response = es.delete_by_query(index=index_name, body=query)
        print(f"response: {response}")
        if response['total'] != 0:
            if response['deleted'] == 1:
                print(f"Successfully deleted document from Elasticsearch. Document ID: {movie_id}")
            else:
                raise Exception()
    except Exception as e:
        print(f"An error occurred while deleting the document in Elasticsearch: {e}")
        raise e