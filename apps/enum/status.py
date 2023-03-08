from django.db.models import TextChoices

from django.utils.translation import gettext_lazy as _

class StatusType(TextChoices):
    Pending = 'Pending',_("Pending")
    Approved = 'Approved',_("Approved")
    Dissapproved = 'Dissapproved',_("Dissapproved")