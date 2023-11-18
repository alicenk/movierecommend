from django.apps import AppConfig


class UsermovierecommendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usermovierecommend'

    def ready(self):
        import usermovierecommend.signals
