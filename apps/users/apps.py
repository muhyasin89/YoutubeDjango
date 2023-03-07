from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TaskReportConfig(AppConfig):
    name="apps.users"
    verbose_name= _("Users")

    def ready(self) -> None:
        # kalau ingin nambah signal
        return super().ready()