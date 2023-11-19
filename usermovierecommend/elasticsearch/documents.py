class UserDocument:
    index = 'users'

    @staticmethod
    def document(instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'surname': instance.surname,
            'email': instance.email
        }


class MovieDocument:
    index = 'movies'

    @staticmethod
    def document(instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'type': instance.type
        }
