from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TaskReportConfig(AppConfig):
    name="apps.task_report"
    verbose_name= _("Task Report")

    def ready(self) -> None:
        # kalau ingin nambah signal
        return super().ready()