
from django.utils.translation import gettext_lazy as _
from django.db.models import (
    CharField,
    TextField,
    BooleanField,
    ForeignKey,
    CASCADE
)
from apps.enum.status import StatusType
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel #for created and updated

User = get_user_model()

class TaskLibrarianDetail(TimeStampedModel):
    name = CharField( _("Name"), max_length=255)
    description = TextField(_("Description"))
    is_finished = BooleanField(default=False)
    status = CharField(
        max_length=50,
        choices=StatusType.choices,
        default=StatusType.Pending,
    )
    approved_by = ForeignKey(User, related_name='approved_by_task_detail', blank=True, null=True, on_delete=CASCADE)
    created_by = ForeignKey(User, related_name='created_by_task_detail', blank=True, null=True, on_delete=CASCADE)

    class Meta:
        db_table="task_librarian_detail"
        verbose_name= _("Task Librarian Details")

    def __str__(self):
        return "{} | {}".format(self.name, self.description)
