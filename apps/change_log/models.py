
from django.utils.translation import gettext_lazy as _
from django.db.models import (
    DateField,
    TextField,
    ForeignKey,
    CASCADE
)


from apps.book.models import Book

from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel #for created and updated

class ChangeLog(TimeStampedModel):
    created_by = ForeignKey(User, related_name='created_by', on_delete=CASCADE)

    class Meta:
        db_table="change_log"
        verbose_name= _("Change Log")