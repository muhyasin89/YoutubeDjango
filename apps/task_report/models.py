
from django.utils.translation import gettext_lazy as _
from django.db.models import (
    CharField,
    ImageField
)

from model_utils.models import TimeStampedModel #for created and updated

class TaskReport(TimeStampedModel):
    file_name = CharField( _("File Name"), max_length=255)
    image = ImageField(_("upload"), upload_to="task_reports/")

    class Meta:
        db_table="task_report"
        verbose_name= _("Task Report")

    def __str__(self):
        return "{} | {}".format(self.file_name)
