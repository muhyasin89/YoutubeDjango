from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RentHistoryConfig(AppConfig):
    name="apps.change_log"
    verbose_name= _("Change Log")

    def ready(self) -> None:
        pass