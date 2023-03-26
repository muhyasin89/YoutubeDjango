from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TaskLibraryDetailConfig(AppConfig):
    name="apps.task_librarian_detail"
    verbose_name= _("Task Librarian Detail")

    def ready(self) -> None:
        try:
            import apps.task_librarian_detail.apps  # noqa F401
        except ImportError:
            pass