
from django.utils.translation import gettext_lazy as _
from django.db.models import (
    CharField,
)

from model_utils.models import TimeStampedModel #for created and updated

class Author(TimeStampedModel):
    name = CharField( _("Name"), max_length=255)

    class Meta:
        db_table="author"
        verbose_name= _("authors")

    def __str__(self):
        return "{} ".format(self.name)