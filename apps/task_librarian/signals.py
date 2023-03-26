from datetime import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.change_log.models import ChangeLog
from apps.task_librarian.models import TaskLibrarian


@receiver(post_save,sender=TaskLibrarian)
def log_update(sender,instance,*args,**kwargs):
    ChangeLog.objects.create(
        section='TaskLibrarian',
        option='Update', # this include create
        created = timezone.now()
    )


@receiver(post_delete,sender=TaskLibrarian)
def log_delete(sender,instance,*args,**kwargs):
    ChangeLog.objects.create(
        section='TaskLibrarian',
        option='Delete',
        created = timezone.now()
    )