from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TaskLibraryConfig(AppConfig):
    name="apps.task_librarian"
    verbose_name= _("Task Librarians")

    def ready(self) -> None:
        try:
            import apps.task_librarian.apps  # noqa F401
        except ImportError:
            pass