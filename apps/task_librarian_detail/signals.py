from datetime import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.change_log.models import ChangeLog
from apps.task_librarian_detail.models import TaskLibrarianDetail



@receiver(post_save,sender=TaskLibrarianDetail)
def log_update(sender,instance,*args,**kwargs):
    ChangeLog.objects.create(
        section='TaskLibrarianDetail',
        option='Update', # this include create
        created = timezone.now()
    )


@receiver(post_delete,sender=TaskLibrarianDetail)
def log_delete(sender,instance,*args,**kwargs):
    ChangeLog.objects.create(
        section='TaskLibrarianDetail',
        option='Delete',
        created = timezone.now()
    )