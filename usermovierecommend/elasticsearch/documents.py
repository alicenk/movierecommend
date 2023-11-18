from elasticsearch_dsl import Document, Text


class UserDocument(Document):
    name = Text()
    surname = Text()
    email = Text()

    class Index:
        name = 'user_index'
