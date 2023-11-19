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
