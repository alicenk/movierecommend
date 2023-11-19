from elasticsearch import Elasticsearch
from django.conf import settings


class ElasticsearchManager:
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super(ElasticsearchManager, cls).__new__(cls)
            cls.instance.es = Elasticsearch(**settings.ELASTICSEARCH_CONNECTION_SETTINGS)
        return cls.instance
