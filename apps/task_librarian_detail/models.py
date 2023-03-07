
from django.utils.translation import gettext_lazy as _
from django.db.models import (
    CharField,
    TextField,
    BooleanField,
    CASCADE
)

from model_utils.models import TimeStampedModel #for created and updated

class TaskLibrarianDetail(TimeStampedModel):
    name = CharField( _("Name"), max_length=255)
    description = TextField(_("Description"))
    is_finished = BooleanField(default=False)

    class Meta:
        db_table="task_librarian_detail"
        verbose_name= _("Task Librarian Details")

    def __str__(self):
        return "{} | {}".format(self.name, self.description)
