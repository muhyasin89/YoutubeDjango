from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CharField
)

import uuid


class User(AbstractUser):
    library_card_number = CharField( _("Library Card Number"), default=uuid.uuid4(),max_length=255)

    def __str__(self):
        return "{}".format(self.library_card_number)