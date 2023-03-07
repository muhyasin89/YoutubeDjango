from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BookConfig(AppConfig):
    name="apps.book"
    verbose_name= _("Books")

    def ready(self) -> None:
        # kalau ingin nambah signal
        return super().ready()