
from django.utils.translation import gettext_lazy as _
from django.db.models import (
    CharField,
    TextField,
    ForeignKey,
    CASCADE
)
from apps.author.models import Author

from model_utils.models import TimeStampedModel #for created and updated

class Book(TimeStampedModel):
    title = CharField( _("Title"), max_length=255)
    description = TextField(_("Description"))
    author = ForeignKey(Author, verbose_name=_("authors"), related_name='books', on_delete=CASCADE)

    class Meta:
        db_table="book"
        verbose_name= _("books")

    def __str__(self):
        return "{} | {}".format(self.title, self.description)