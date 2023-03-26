from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthorConfig(AppConfig):
    name="apps.author"
    verbose_name= _("Author")

    def ready(self) -> None:
        try:
            import apps.author.apps  # noqa F401
        except ImportError:
            pass