
from django.utils.translation import gettext_lazy as _
from django.db.models import (
    CharField,
    ImageField,
    ForeignKey,
    CASCADE
)
from apps.enum.status import StatusType
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel #for created and updated


User = get_user_model()
class TaskReport(TimeStampedModel):
    file_name = CharField( _("File Name"), max_length=255)
    image = ImageField(_("upload"), upload_to="task_reports/")
    status =   CharField(
        max_length=50,
        choices=StatusType.choices,
        default=StatusType.Pending,
    )
    approved_by = ForeignKey(User, related_name='approved_by_task_report', blank=True, null=True, on_delete=CASCADE)
    created_by = ForeignKey(User, related_name='created_by_task_report',blank=True, null=True, on_delete=CASCADE)


    class Meta:
        db_table="task_report"
        verbose_name= _("Task Report")

    def __str__(self):
        return "{} | {}".format(self.file_name)
