from datetime import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.book.models import Book
from apps.change_log.models import ChangeLog



@receiver(post_save,sender=Book)
def log_update(sender,instance,*args,**kwargs):
    ChangeLog.objects.create(
        section='Book',
        option='Update', # this include create
        created = timezone.now()
    )


@receiver(post_delete,sender=Book)
def log_delete(sender,instance,*args,**kwargs):
    ChangeLog.objects.create(
        section='RentHistory',
        option='Delete',
        created = timezone.now()
    )