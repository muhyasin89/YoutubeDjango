
from django.utils.translation import gettext_lazy as _
from django.db.models import (
    ForeignKey,
    CharField,
    CASCADE
)

from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel

from apps.enum.change_log import ActivityType, SectionType #for created and updated

class ChangeLog(TimeStampedModel):
    section_status = CharField(
        max_length=50,
        choices=SectionType.choices,
        default=SectionType.Other,
    )
     
    activity_status = CharField(
        max_length=50,
        choices=ActivityType.choices,
        default=ActivityType.Other,
    )

    created_by = ForeignKey(User, related_name='created_by', on_delete=CASCADE)

    class Meta:
        db_table="change_log"
        verbose_name= _("Change Log")