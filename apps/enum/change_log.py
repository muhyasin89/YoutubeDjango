from django.db.models import TextChoices

from django.utils.translation import gettext_lazy as _

class SectionType(TextChoices):
    Other = 'Other', _("Other")
    Book = 'Book',_("Book")
    Author = 'Author',_("Author")
    RentHistory = 'RentHistory',_("Rent History")
    TaskLibrarian = 'TaskLibrarian',_("Task Librarian")
    TaskLibrarianDetail = 'TaskLibrarianDetail',_("TaskLibrarian Detail")
    TaskReport = 'TaskReport',_("Task Report")


class ActivityType(TextChoices):
    Other = 'Other', _("Other")
    Update = 'Update',_("Update")
    Delete = 'Delete',_("Not Delete")
