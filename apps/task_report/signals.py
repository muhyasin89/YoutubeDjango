from datetime import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.change_log.models import ChangeLog
from apps.task_report.models import TaskReport

@receiver(post_save,sender=TaskReport)
def log_update(sender,instance,*args,**kwargs):
    ChangeLog.objects.create(
        section='TaskReport',
        option='Update', # this include create
        created = timezone.now()
    )


@receiver(post_delete,sender=TaskReport)
def log_delete(sender,instance,*args,**kwargs):
    ChangeLog.objects.create(
        section='TaskReport',
        option='Delete',
        created = timezone.now()
    )