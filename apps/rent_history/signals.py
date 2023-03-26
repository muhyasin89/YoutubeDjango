from datetime import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.change_log.models import ChangeLog

from apps.rent_history.models import RentHistory


@receiver(post_save,sender=RentHistory)
def log_update(sender,instance,*args,**kwargs):
    ChangeLog.objects.create(
        section='RentHistory',
        option='Update', # this include create
        created = timezone.now()
    )


@receiver(post_delete,sender=RentHistory)
def log_delete(sender,instance,*args,**kwargs):
    ChangeLog.objects.create(
        section='RentHistory',
        option='Delete',
        created = timezone.now()
    )