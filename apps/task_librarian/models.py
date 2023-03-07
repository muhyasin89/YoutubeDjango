
from django.utils.translation import gettext_lazy as _
from django.db.models import (
    CharField,
    TextField,
    ManyToManyField
)
from apps.task_librarian_detail.models import TaskLibrarianDetail
from apps.task_report.models import TaskReport

from model_utils.models import TimeStampedModel #for created and updated

class TaskLibrarian(TimeStampedModel):
    name = CharField( _("Name"), max_length=255)
    description = TextField(_("Description"))
    task_detail = ManyToManyField(TaskLibrarianDetail)
    report = ManyToManyField(TaskReport)

    class Meta:
        db_table="task_librarian"
        verbose_name= _("Task Librarian")

    def __str__(self):
        return "{} | {}".format(self.name, self.description)
