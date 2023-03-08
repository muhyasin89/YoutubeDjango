from django.db.models import TextChoices

from django.utils.translation import gettext_lazy as _

class RentStatusType(TextChoices):
    Not_Rent = 'Not_Rent',_("Not Rent")
    Rent = 'Rent',_("Rent")
