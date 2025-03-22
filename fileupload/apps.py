from django.apps import AppConfig

class FileUploadAppConfig(AppConfig):
    """
        This is app configuration for fileupload app
    """
    name = 'fileupload'

    def ready(self):
        import fileupload.signals # import and enable signal for Audit log creation