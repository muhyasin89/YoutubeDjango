
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

class RentHistory(TimeStampedModel):
    user = ForeignKey(User, related_name='user_rent_history', on_delete=CASCADE)
    book = ForeignKey(Book, related_name='book_rent_history', on_delete=CASCADE)
    date_borrow = DateField()
    date_return = DateField()
    description = TextField(_("Description"))