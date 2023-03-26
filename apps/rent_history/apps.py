from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RentHistoryConfig(AppConfig):
    name="apps.rent_history"
    verbose_name= _("Rent Histories")

    def ready(self) -> None:
        try:
            import apps.rent_history.apps  # noqa F401
        except ImportError:
            pass