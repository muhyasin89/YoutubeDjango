from django.db.models import TextChoices

from django.utils.translation import gettext_lazy as _

class ActiveType(TextChoices):
    Active = 'Active',_("Active")
    Not_Active = 'Not_Active',_("Not Active")