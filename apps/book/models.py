
from django.utils.translation import gettext_lazy as _
from django.db.models import (
    CharField,
    TextField,
    ForeignKey,
    ImageField,
    CASCADE
)
from apps.author.models import Author
from apps.enum.status import StatusType
from apps.enum.rent_status import RentStatusType
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel #for created and updated

User = get_user_model()

class Book(TimeStampedModel):
    title = CharField( _("Title"), max_length=255)
    description = TextField(_("Description"))
    thumbnail_image = ImageField(upload_to="books", null=True, blank=True)
    status = CharField(
        max_length=50,
        choices=StatusType.choices,
        default=StatusType.Pending,
    )

    rent_status = CharField(
        max_length=50,
        choices=RentStatusType.choices,
        default=RentStatusType.Not_Rent,
    )
    author = ForeignKey(Author, verbose_name=_("authors"), related_name='author_books', on_delete=CASCADE)
    approved_by = ForeignKey(User, related_name='approved_by_books', blank=True, null=True, on_delete=CASCADE)
    created_by = ForeignKey(User, related_name='created_by_books', blank=True, null=True, on_delete=CASCADE)

    class Meta:
        db_table="book"
        verbose_name= _("books")

    def __str__(self):
        return "{} | {}".format(self.title, self.description)