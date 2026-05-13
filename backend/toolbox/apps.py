# toolbox/apps.py
from django.apps import AppConfig

class ToolboxConfig(AppConfig):
    name = 'toolbox'

    def ready(self) -> None:
        import toolbox.spectacular_extensions  # noqa: F401