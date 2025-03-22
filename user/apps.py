from django.apps import AppConfig

class UserAppConfig(AppConfig):
    name = 'user'

    def ready(self):
        import user.signals # import and enable signals in user app