from django.apps import AppConfig


class GongmoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gongmo'

    def ready(self):
        try:
            import gongmo.tasks
        except ImportError:
            pass